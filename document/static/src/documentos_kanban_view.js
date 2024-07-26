/** @odoo-module */

import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view";
import { KanbanController } from "@web/views/kanban/kanban_controller";
import { useService } from "@web/core/utils/hooks";

const { onWillStart } = owl


class DocumentosKanbanController extends KanbanController {
    setup(){
        super.setup()
        console.log("this is documentos kanbanview")       

        this.orm = useService("orm")
    
        onWillStart(async ()=>{
            this.carpetasDocumentos = await this.orm.readGroup("documentos.carpetas", [], ['nombre_completo'],['carpeta_padre'])
            console.log(this.carpetasDocumentos)
        })
    }



    


}


DocumentosKanbanController.template = 'owl.DocumentosKanbanView'


export const documentosKanbanView = {
    ...kanbanView,
    Controller: DocumentosKanbanController
}


registry.category("views").add("documentos_kanban_view", documentosKanbanView)
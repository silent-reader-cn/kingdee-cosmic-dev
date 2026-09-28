# 签字任务-plmdc_signature_task

## 签字任务-主表 t_plmdc_signature_task

- **表名称：** 签字任务-主表
- **表名：** t_plmdc_signature_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmixedsignmodels | 签字图片组 | varchar | 255 |  | √ | ' ' | 签字图片组 |
| 3 | fsignorder | 签字序号 | int4 | 32 |  | √ | 0 | 签字序号 |
| 4 | fcontrolledsealsignvalue | 受控章的值 | varchar | 255 |  | √ | ' ' | 受控章的值 |
| 5 | fcontrolledsealmark | 受控章标识 | varchar | 50 |  | √ | ' ' | 受控章标识 |
| 6 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: wait :等待 ongoing :进行中 fail :失败 complete :转换完成 |
| 7 | fversionmark | 版本标记 | varchar | 50 |  | √ | ' ' | 版本标记 |
| 8 | fwfcodeid | 流程节点id | varchar | 50 |  | √ | ' ' | 流程节点id |
| 9 | fremarkvalue | 意见的值 | varchar | 255 |  | √ | ' ' | 意见的值 |
| 10 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 11 | fsignaturefileid | 签字文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 12 | fbatchno | 批次号 | int8 | 64 |  | √ | 0 | 批次号 |
| 13 | fcreatetime | 创建时间 | int8 | 64 |  | √ | 0 | 创建时间 |
| 14 | fversionvalue | 版本的值 | varchar | 255 |  | √ | ' ' | 版本的值 |
| 15 | fsignmark | 签字标识 | varchar | 50 |  | √ | ' ' | 签字标识 |
| 16 | fdocid | 逻辑文档 | int8 | 64 |  | √ | 0 | [文档版本 plm_pdm_document_revision](../plmsm_files/plm_pdm_document_revision.md) |
| 17 | fwfexecutionid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 18 | ftimevalue | 时间的值 | varchar | 50 |  | √ | ' ' | 时间的值 |
| 19 | fsignvalue | 签字值 | varchar | 255 |  | √ | ' ' | 签字值 |
| 20 | fmixedsignmodels_tag | 签字图片组_详情 | text | 0 |  |  | null | 签字图片组_详情 |
| 21 | fsignconfiguration | 签名配置方式 | varchar | 50 |  | √ | ' ' | 签名配置方式,枚举: bookmark :书签配置 coordinate :坐标配置 |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | ftaskid | 任务ID | varchar | 50 |  | √ | ' ' | 任务ID |
| 24 | fremarkmark | 意见标记 | varchar | 50 |  | √ | ' ' | 意见标记 |
| 25 | fsigntype | 签字类型 | int4 | 32 |  | √ | 0 | 签字类型 |
| 26 | ftimemark | 时间标记 | varchar | 50 |  | √ | ' ' | 时间标记 |
| 27 | fsourcefileid | 原文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_signature_task |  | fid |
| 2 | idx_signature_task_taskid |  | ftaskid |

---

## 流程坐标配置映射-子表 t_plmdc_signature_entity

- **表名称：** 流程坐标配置映射-子表
- **表名：** t_plmdc_signature_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfiguration | 配置内容 | varchar | 50 |  | √ | ' ' | 配置内容,枚举: signbook :签名书签 datebook :日期书签 auditbook :审批意见书签 docrevbook :文档版本书签 stampsignbook :签章书签 |
| 3 | fx | X轴 | numeric | 23 | 2 | √ | 0 | X轴 |
| 4 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: PDF :PDF Solidworks :Solidworks Creo :Creo Catia :Catia UG :UG Autocad :Autocad 中望2D :中望2D |
| 5 | fy | Y轴 | numeric | 23 | 2 | √ | 0 | Y轴 |
| 6 | fscale | 缩放比例 | numeric | 23 | 2 | √ | 0 | 缩放比例 |
| 7 | fdrawing | 图纸方向 | varchar | 50 |  | √ | ' ' | 图纸方向,枚举: horizontal :横向 vertical :纵向 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fheight | 高度 | numeric | 23 | 2 | √ | 0 | 高度 |
| 10 | ftabsize | 页面大小 | varchar | 50 |  | √ | ' ' | 页面大小,枚举: a4 :a4 a3 :a3 a2 :a2 a1 :a1 a0 :a0 |
| 11 | fwidth | 宽度 | numeric | 23 | 2 | √ | 0 | 宽度 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_signature_entity |  | fid |
| 2 | pk_t_plmdc_signature_entity |  | fentryid |

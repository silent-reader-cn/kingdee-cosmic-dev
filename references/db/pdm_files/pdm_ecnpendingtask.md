# ECN待办任务-pdm_ecnpendingtask

## ECN待办任务-多语言表 t_pdm_ecnpendingtask_l

- **表名称：** ECN待办任务-多语言表
- **表名：** t_pdm_ecnpendingtask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_ecnpendingtask_l |  | fid,flocaleid |
| 2 | pk_t_pdm_ecnpendingtask_l |  | fpkid |

---

## ECN待办任务-主表 t_pdm_ecnpendingtask

- **表名称：** ECN待办任务-主表
- **表名：** t_pdm_ecnpendingtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料主档 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcurrreverseqty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 5 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fneedchangereverseqty | 预留数量增减调整 | numeric | 23 | 10 | √ | 0 | 预留数量增减调整 |
| 9 | fbizbill | 业务单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | funreverseqty | 未预留数量 | numeric | 23 | 10 | √ | 0 | 未预留数量 |
| 11 | fpendingtype | 待办类型 | bpchar | 1 |  | √ | '0' | 待办类型,枚举: 0 :新增 1 :修改 2 :删除 |
| 12 | fecoorderseq | 工程变更单行号 | int4 | 32 |  | √ | 0 | 工程变更单行号 |
| 13 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | fbillno | 任务编号 | varchar | 30 |  | √ | ' ' | 任务编号 |
| 15 | fmaterialplanid | 物料编码 | int8 | 64 |  | √ | 0 | [物料计划信息 mpdm_materialplan](../sbd_files/mpdm_materialplan.md) |
| 16 | fadjustquantity | 数量调整为 | numeric | 23 | 10 | √ | 0 | 数量调整为 |
| 17 | forderseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fassignstatus | 任务指派状态 | varchar | 30 |  | √ | ' ' | 任务指派状态,枚举: A :未指派 B :已指派 |
| 20 | fbillstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 制单时间 | timestamp | 0 |  |  | null | 制单时间 |
| 22 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fexecutestatus | 任务执行状态 | varchar | 30 |  | √ | ' ' | 任务执行状态,枚举: A :未开始 B :进行中 C :已完成 D :挂起 E :已关闭 |
| 24 | fecoapplyorder | 工程变更申请单 | varchar | 50 |  | √ | ' ' | 工程变更申请单 |
| 25 | fmaterialpurid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 26 | finitiatorid | 任务发起人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | forderno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 28 | fecoapplyseq | 工程变更申请单行号 | int4 | 32 |  | √ | 0 | 工程变更申请单行号 |
| 29 | fmaterialmftid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 30 | fecoorderno | 工程变更单 | varchar | 50 |  | √ | ' ' | 工程变更单 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_ecnpendingtask |  | fid |
| 2 | idx_pdm_ecnpendingtask_org |  | forgid,fbillno |

---

## 任务执行人-多选基础资料表 t_pdm_ecntaskexecutor

- **表名称：** 任务执行人-多选基础资料表
- **表名：** t_pdm_ecntaskexecutor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_ecntaskexecutor |  | fpkid |
| 2 | idx_pdm_ecntaskexecutor |  | fid |

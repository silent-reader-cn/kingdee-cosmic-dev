# 审查结果-clm_mscon_examinerecord

## 单据体-子表 t_mscon_examineentry

- **表名称：** 单据体-子表
- **表名：** t_mscon_examineentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexamineitems | 审查项 | int8 | 64 |  | √ | 0 | [审查项 clm_mscon_examineitems](../clmrv_files/clm_mscon_examineitems.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fpropose | 建议 | varchar | 512 |  | √ | ' ' | 建议 |
| 4 | finspectdata | 审查结果 | varchar | 255 |  | √ | ' ' | 审查结果 |
| 5 | fexaminestatus | 审查状态 | varchar | 50 |  | √ | ' ' | 审查状态,枚举: A :通过 B :未通过 C :异常 |
| 6 | frisk | 风险 | varchar | 512 |  | √ | ' ' | 风险 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fiteminfo | 元数据 | varchar | 255 |  | √ | ' ' | 元数据 |
| 9 | finspectdata_tag | 审查结果_详情 | text | 0 |  |  | null | 审查结果_详情 |
| 10 | fiteminfo_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mscon_examineentry_fk |  | fid |
| 2 | pk_mscon_examineentry |  | fentryid |

---

## 审查结果-主表 t_mscon_examinerecord

- **表名称：** 审查结果-主表
- **表名：** t_mscon_examinerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexamineplan | 审查方案 | int8 | 64 |  | √ | 0 | [审查方案 clm_mscon_aiexaminescheme](../clmrv_files/clm_mscon_aiexaminescheme.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexecutionstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 0 :执行成功 1 :执行失败 2 :执行中 3 :执行终止 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fexamsrcbillid | 审查来源单据id | int8 | 64 |  | √ | 0 | 审查来源单据id |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fbiztimeend | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 11 | fexamsrcentity | 审查来源实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fexamineplanjson_tag | 审查方案_详情 | text | 0 |  |  | null | 审查方案_详情 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ftimeconsum | 耗时/秒 | int8 | 64 |  | √ | 0 | 耗时/秒 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fexamsrcbill | 审查来源单据 | varchar | 512 |  | √ | ' ' | 审查来源单据 |
| 17 | fexampassedtems | 审查通过审查项 | int8 | 64 |  | √ | 0 | 审查通过审查项 |
| 18 | fexamineplanjson | 审查方案 | varchar | 255 |  | √ | ' ' | 审查方案 |
| 19 | fbiztimebegin | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fexamfailedtems | 审查未通过审查项 | int8 | 64 |  | √ | 0 | 审查未通过审查项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mscon_examinerecord |  | fid |
| 2 | idx_mscon_examinerecord_m0 |  | fbillno |

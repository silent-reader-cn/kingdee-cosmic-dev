# 计划编制版本物料详情-psw_mtlmstrschdver

## 数量明细-子表 t_psw_mtlmstrschdverdet

- **表名称：** 数量明细-子表
- **表名：** t_psw_mtlmstrschdverdet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartdatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 3 | fenddatetime | 截止时间 | timestamp | 0 |  |  | null | 截止时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftotalqtytostart | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_mtlmsvdetfk |  | fid |
| 2 | pk_t_psw_mtlmstrschdverdet |  | fentryid |

---

## 计划编制版本物料详情-主表 t_psw_mtlmstrschdver

- **表名称：** 计划编制版本物料详情-主表
- **表名：** t_psw_mtlmstrschdver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fversion | 版本 | int8 | 64 |  | √ | 0 | 计划编制版本 psw_mstrschdversion |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_mtlmstrschdver |  | fid |
| 2 | idx_t_psw_mtlmsv |  | fversion,fmaterial,fmaterialversion,fauxpty |

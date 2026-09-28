# 匿名基础资料配置-adm_basedataconfig

## 单据体-子表 t_pur_baseconfigentry

- **表名称：** 单据体-子表
- **表名：** t_pur_baseconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fguestbasedatano | 基础资料字段标识 | varchar | 30 |  | √ | ' ' | 基础资料字段标识 |
| 3 | fismultiple | 支持多选 | bpchar | 1 |  | √ | '0' | 支持多选 |
| 4 | fcustomdatasource | 自定义数据源加载插件 | varchar | 255 |  | √ | ' ' | 自定义数据源加载插件 |
| 5 | fentryno | 分录标识 | varchar | 30 |  | √ | ' ' | 分录标识 |
| 6 | fsourcebasedatano | 基础资料原标识 | varchar | 30 |  | √ | ' ' | 基础资料原标识 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fisentryfield | 是否分录字段 | bpchar | 1 |  | √ | '0' | 是否分录字段 |
| 11 | fselects | 查询字段 | varchar | 512 |  | √ | ' ' | 查询字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_baseconfigentry |  | fentryid |
| 2 | idx_pur_baseconfigentry_fid |  | fid,fseq |

---

## 匿名基础资料配置-主表 t_pur_pbdbasedataconfig

- **表名称：** 匿名基础资料配置-主表
- **表名：** t_pur_pbdbasedataconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmainentity | 单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_baseconfig_fcreate |  | fcreatetime |
| 2 | pk_t_pur_pbdbasedataconfig |  | fid |

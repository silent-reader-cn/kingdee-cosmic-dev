# 报告参数数据源-ippm_paramdatasource

## 关联属性单据体-子表 t_ippm_paramrefentry

- **表名称：** 关联属性单据体-子表
- **表名：** t_ippm_paramrefentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fmainattr | 主数据源属性 | varchar | 50 |  | √ | ' ' | 主数据源属性,枚举: |
| 4 | fchildattr | 子数据源属性 | varchar | 50 |  | √ | ' ' | 子数据源属性,枚举: |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_paramrefentry |  | fentryid |
| 2 | idx_ippm_paramrefentry |  | fid |

---

## 数据字段单据体-子表 t_ippm_paramfieldentry

- **表名称：** 数据字段单据体-子表
- **表名：** t_ippm_paramfieldentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 4 :数值 -9 :文本 93 :时间 12 :枚举 list :列表 |
| 3 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffieldsign | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | frefattr | 关联属性 | varchar | 50 |  | √ | ' ' | 关联属性,枚举: |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_paramfieldentry |  | fentryid |
| 2 | idx_ippm_paramfieldentry |  | fid |

---

## 报告参数数据源-主表 t_ippm_paramdatasource

- **表名称：** 报告参数数据源-主表
- **表名：** t_ippm_paramdatasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: base :基础数据 combine :组合 fix :固定值 page :配置页面 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmainsourceid | 主数据源 | int8 | 64 |  | √ | 0 | [报告参数数据源 ippm_paramdatasource](../ippm_files/ippm_paramdatasource.md) |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fchildsourceid | 子数据源 | int8 | 64 |  | √ | 0 | [报告参数数据源 ippm_paramdatasource](../ippm_files/ippm_paramdatasource.md) |
| 11 | ffilterdata | 过滤数据 | varchar | 2000 |  | √ | ' ' | 过滤数据 |
| 12 | fbizentityid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_paramdatasource |  | fnumber |
| 2 | pk_t_ippm_paramdatasource |  | fid |

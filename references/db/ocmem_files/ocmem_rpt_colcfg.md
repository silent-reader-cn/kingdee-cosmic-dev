# 营销费用分析过滤字段配置-ocmem_rpt_colcfg

## 营销费用分析过滤字段配置-主表 t_ocmem_rptcfg

- **表名称：** 营销费用分析过滤字段配置-主表
- **表名：** t_ocmem_rptcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_rptcfg_createrid |  | fcreaterid |
| 2 | pk_ocmem_rptcfg |  | fid |

---

## 字段关系映射-子表 t_ocmem_rptcfgentry

- **表名称：** 字段关系映射-子表
- **表名：** t_ocmem_rptcfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatatimecol | 过滤时间字段 | varchar | 80 |  | √ | ' ' | 过滤时间字段 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsrcentity | 来源实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frepocol | 原时间字段 | varchar | 80 |  | √ | ' ' | 原时间字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_rptcfgentry_fid |  | fid |
| 2 | pk_ocmem_rptcfgentry |  | fentryid |

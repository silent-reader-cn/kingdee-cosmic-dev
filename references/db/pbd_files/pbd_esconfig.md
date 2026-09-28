# 全文检索配置-pbd_esconfig

## 全文检索配置-主表 t_pbd_esconfig

- **表名称：** 全文检索配置-主表
- **表名：** t_pbd_esconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | findexentityid | 索引实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | findexkey | 索引标识 | varchar | 50 |  | √ | ' ' | 索引标识 |
| 7 | fparentesconfigid | 父配置 | int8 | 64 |  | √ | 0 | 全文检索配置 pbd_esconfig |
| 8 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fishandlebyparent | 父配置触发 | bpchar | 1 |  | √ | '0' | 父配置触发 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fesoutputid | 结果输出对象 | int8 | 64 |  | √ | 0 | 全文检索输出 pbd_esoutput |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fregion | 索引分区 | varchar | 50 |  | √ | ' ' | 索引分区 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_esconfig_fnumber |  | fnumber |
| 2 | pk_t_pbd_esconfig |  | fid |

---

## 聚合单据体-子表 t_pbd_esconfigaggentry

- **表名称：** 聚合单据体-子表
- **表名：** t_pbd_esconfigaggentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fesaggregationid | 聚合编码 | int8 | 64 |  | √ | 0 | 全文检索聚合 pbd_esaggregation |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_esconfigaggentry |  | fentryid |
| 2 | idx_pbd__esconfigaggentry_id |  | fid |

---

## 全文检索配置-多语言表 t_pbd_esconfig_l

- **表名称：** 全文检索配置-多语言表
- **表名：** t_pbd_esconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_esconfig_l |  | fpkid |
| 2 | idx_pbd_esconfig_l_fid |  | fid |

---

## 属性单据体-子表 t_pbd_esconfigentry

- **表名称：** 属性单据体-子表
- **表名：** t_pbd_esconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fesmappingid | es属性编码 | int8 | 64 |  | √ | 0 | 全文检索映射属性 pbd_esmapping_property |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fisprimarykey | 是否主键 | bpchar | 1 |  | √ | '0' | 是否主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_esconfigentry_id |  | fid |
| 2 | pk_t_pbd_esconfigentry |  | fentryid |

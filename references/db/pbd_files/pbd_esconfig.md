# 全文检索配置-pbd_esconfig

## 索引配置参数单据体-子表 t_pbd_esconfigindexentry

- **表名称：** 索引配置参数单据体-子表
- **表名：** t_pbd_esconfigindexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 值 | varchar | 2000 |  | √ | ' ' | 值 |
| 3 | fparamname | 配置名称 | varchar | 80 |  | √ | ' ' | 配置名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparamtype | 配置类型 | varchar | 50 |  | √ | ' ' | 配置类型,枚举: int :整数 string :字符串 json :JSON |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_esconfigindexentry |  | fentryid |
| 2 | idx_pbd_esindexentry_id |  | fid,fseq |

---

## 全文检索配置-主表 t_pbd_esconfig

- **表名称：** 全文检索配置-主表
- **表名：** t_pbd_esconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 152 |  | √ | ' ' | 名称 |
| 4 | findexentityid | 索引实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | findexkey | 索引标识 | varchar | 50 |  | √ | ' ' | 索引标识 |
| 7 | fparentesconfigid | 父配置 | int8 | 64 |  | √ | 0 | [全文检索配置 pbd_esconfig](../pbd_files/pbd_esconfig.md) |
| 8 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fishandlebyparent | 父配置触发 | bpchar | 1 |  | √ | '0' | 父配置触发 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fesoutputid | 结果输出对象 | int8 | 64 |  | √ | 0 | [全文检索输出 pbd_esoutput](../pbd_files/pbd_esoutput.md) |
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
| 2 | fesaggregationid | 聚合编码 | int8 | 64 |  | √ | 0 | [全文检索聚合 pbd_esaggregation](../pbd_files/pbd_esaggregation.md) |
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

## 搜索查询排序单据体-子表 t_pbd_esconfigsortentry

- **表名称：** 搜索查询排序单据体-子表
- **表名：** t_pbd_esconfigsortentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscript | 脚本 | varchar | 2000 |  | √ | ' ' | 脚本 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fessortnumber | es属性编码 | varchar | 50 |  | √ | ' ' | es属性编码 |
| 5 | fscripttype | 脚本排序类型 | varchar | 50 |  | √ | ' ' | 脚本排序类型,枚举: number :数字 string :字符 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fnestsnumber | 嵌套属性 | varchar | 50 |  | √ | ' ' | 嵌套属性 |
| 8 | fessortby | 排序 | varchar | 50 |  | √ | ' ' | 排序,枚举: asc :升序 desc :降序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_essortentry_id |  | fid,fseq |
| 2 | pk_pbd_esconfigsortentry |  | fentryid |

---

## 全文检索配置-多语言表 t_pbd_esconfig_l

- **表名称：** 全文检索配置-多语言表
- **表名：** t_pbd_esconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 152 |  | √ | ' ' | 名称 |
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
| 3 | fesmappingid | es属性编码 | int8 | 64 |  | √ | 0 | [全文检索映射属性 pbd_esmapping_property](../pbd_files/pbd_esmapping_property.md) |
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

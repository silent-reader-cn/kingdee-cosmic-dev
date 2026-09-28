# 全文检索聚合-pbd_esaggregation

## 全文检索聚合-多语言表 t_pbd_esaggs_l

- **表名称：** 全文检索聚合-多语言表
- **表名：** t_pbd_esaggs_l

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
| 1 | pk_t_pbd_esaggs_l |  | fpkid |
| 2 | idx_pbd_esaggs_l_fid |  | fid |

---

## 聚合结果单据体-子表 t_pbd_esaggs_output

- **表名称：** 聚合结果单据体-子表
- **表名：** t_pbd_esaggs_output

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fevalpath | 取值表达式 | varchar | 255 |  | √ | ' ' | 取值表达式 |
| 3 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 |
| 4 | fisarray | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffixevalue | 直接赋值 | varchar | 255 |  | √ | ' ' | 直接赋值 |
| 9 | ffieldkey | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_esaggs_output |  | fentryid |
| 2 | idx_pbd_esaggs_output_id |  | fid |

---

## 子聚合-多选基础资料表 t_pbd_esaggs_sub

- **表名称：** 子聚合-多选基础资料表
- **表名：** t_pbd_esaggs_sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [全文检索聚合 pbd_esaggregation](../pbd_files/pbd_esaggregation.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_esaggs_sub_fid |  | fid |
| 2 | pk_t_pbd_esaggs_sub |  | fpkid |

---

## 全文检索聚合-主表 t_pbd_esaggs

- **表名称：** 全文检索聚合-主表
- **表名：** t_pbd_esaggs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | findexentityid | 索引实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fparams | 参数设置 | varchar | 2000 |  | √ | ' ' | 参数设置 |
| 7 | ffieldid | 字段 | int8 | 64 |  | √ | 0 | [全文检索映射属性 pbd_esmapping_property](../pbd_files/pbd_esmapping_property.md) |
| 8 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsize | 数量 | int4 | 32 |  | √ | 0 | 数量 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fpath | 嵌套路径 | varchar | 50 |  | √ | ' ' | 嵌套路径 |
| 16 | fesaggtypeid | 聚合类型 | int8 | 64 |  | √ | 0 | [全文检索聚合类型 pbd_esaggtype](../pbd_files/pbd_esaggtype.md) |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | ffilters | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_esaggs_fnumber |  | fnumber |
| 2 | pk_t_pbd_esaggs |  | fid |

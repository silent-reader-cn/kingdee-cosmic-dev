# 可销控制扩展定义-ocdbd_salectrl_extdefine

## 可销控制扩展定义-多语言表 t_ocdbd_salectrl_ext_l

- **表名称：** 可销控制扩展定义-多语言表
- **表名：** t_ocdbd_salectrl_ext_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_salectrl_ext_l_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_salectrl_ext_l |  | fpkid |

---

## 可销控制扩展定义-主表 t_ocdbd_salectrl_ext

- **表名称：** 可销控制扩展定义-主表
- **表名：** t_ocdbd_salectrl_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_salectrl_ext |  | fid |
| 2 | idx_ocdbd_salectrl_ext_mid |  | fmasterid |

---

## 查询条件匹配规则-子表 t_ocdbd_salectrl_query

- **表名称：** 查询条件匹配规则-子表
- **表名：** t_ocdbd_salectrl_query

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffulldestcol | 可销控制表字段全标识 | varchar | 100 |  | √ | ' ' | 可销控制表字段全标识 |
| 3 | fdestcol | 可销控制表字段标识 | varchar | 100 |  | √ | ' ' | 可销控制表字段标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparamtype | 输入条件 | varchar | 10 |  | √ | ' ' | 输入条件,枚举: 1 :销售组织 2 :销售渠道 3 :订货渠道 |
| 6 | ffullsrccol | 条件属性全标识 | varchar | 100 |  | √ | ' ' | 条件属性全标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fconverttype | 值匹配方式 | varchar | 10 |  | √ | ' ' | 值匹配方式,枚举: 1 :等于 2 :大于 3 :大于等于 4 :小于 5 :小于等于 6 :在......中 |
| 9 | fsrccol | 条件属性标识 | varchar | 100 |  | √ | ' ' | 条件属性标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_salectrl_query |  | fentryid |
| 2 | idx_ocdbd_salectrl_query_fid |  | fid |

---

## 输出结果匹配规则-子表 t_ocdbd_salectrl_result

- **表名称：** 输出结果匹配规则-子表
- **表名：** t_ocdbd_salectrl_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffulldestcol | 可销控制表字段全标识 | varchar | 100 |  | √ | ' ' | 可销控制表字段全标识 |
| 3 | fdestcol | 可销控制表字段标识 | varchar | 100 |  | √ | ' ' | 可销控制表字段标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparamtype | 输出结果 | varchar | 10 |  | √ | ' ' | 输出结果,枚举: 1 :商品 |
| 6 | ffullsrccol | 结果属性全标识 | varchar | 100 |  | √ | ' ' | 结果属性全标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fconverttype | 值匹配方式 | varchar | 10 |  | √ | ' ' | 值匹配方式,枚举: 1 :等于 2 :大于 3 :大于等于 4 :小于 5 :小于等于 6 :在......中 |
| 9 | fsrccol | 结果属性标识 | varchar | 100 |  | √ | ' ' | 结果属性标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_salectrl_result_fid |  | fid |
| 2 | pk_ocdbd_salectrl_result |  | fentryid |

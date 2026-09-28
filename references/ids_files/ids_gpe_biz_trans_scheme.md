# 结果下推方案-ids_gpe_biz_trans_scheme

## 单据体-子表 t_ids_gpe_biztrans_field

- **表名称：** 单据体-子表
- **表名：** t_ids_gpe_biztrans_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizobjfield | 业务对象字段 | varchar | 255 |  | √ | ' ' | 业务对象字段,枚举: |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fquotefield | 引用数据字段 | varchar | 100 |  | √ | ' ' | 引用数据字段,枚举: |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_gpe_biztrans_field |  | fentryid |
| 2 | idx_ids_gpe_trans_field_fid |  | fid |

---

## 结果下推方案-多语言表 t_ids_gpe_biztrans_scheme_l

- **表名称：** 结果下推方案-多语言表
- **表名：** t_ids_gpe_biztrans_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_gpe_biztrans_scheme_l |  | fpkid |
| 2 | idx_ids_gpe_t_scheme_l_fname |  | fname |

---

## 结果下推方案-主表 t_ids_gpe_biztrans_scheme

- **表名称：** 结果下推方案-主表
- **表名：** t_ids_gpe_biztrans_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | freceivenotice | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 4 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :禁用 1 :可用 |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpredictrecord | 预测结果 | int8 | 64 |  | √ | 0 | 预测结果 ids_gpe_predict_record |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | feventnumber | 事件编码 | varchar | 50 |  | √ | ' ' | 事件编码 |
| 10 | fscheme | 预测模型方案 | int8 | 64 |  | √ | 0 | 预测模型方案 ids_gpe_scheme |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fbizobj | 目标业务对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | ffiltercondition | 过滤条件 | varchar | 512 |  | √ | ' ' | 过滤条件 |
| 14 | fcustomparams | 自定义参数 | varchar | 255 |  | √ | ' ' | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_gpe_biztrans_scheme |  | fid |
| 2 | idx_ids_gpe_trans_scheme_name |  | fname |

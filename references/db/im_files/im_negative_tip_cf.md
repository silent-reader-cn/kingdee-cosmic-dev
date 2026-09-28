# 负库存提示配置-im_negative_tip_cf

## 负库存提示配置-多语言表 t_im_negative_tip_cf_l

- **表名称：** 负库存提示配置-多语言表
- **表名：** t_im_negative_tip_cf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_negative_tip_cf_l |  | fpkid |
| 2 | idx_im_negative_tip_cf_l_0 |  | fid,flocaleid |

---

## 维度配置-子表 t_im_negative_tip_cols

- **表名称：** 维度配置-子表
- **表名：** t_im_negative_tip_cols

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbalfieldname | 余额表字段名称 | varchar | 50 |  | √ | ' ' | 余额表字段名称 |
| 3 | ftipcol | 提示维度 | bpchar | 1 |  | √ | '0' | 提示维度 |
| 4 | fshowprop | 显示属性 | varchar | 50 |  | √ | ' ' | 显示属性,枚举: 1 :编码 2 :名称 3 :编码+名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbalfield | 余额表字段标识 | varchar | 50 |  | √ | ' ' | 余额表字段标识 |
| 8 | fbasedataprop | 基础资料 | bpchar | 1 |  | √ | '0' | 基础资料 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_negative_tip_cols_fk |  | fid |
| 2 | pk_t_im_negative_tip_cols |  | fentryid |

---

## 负库存提示配置-主表 t_im_negative_tip_cf

- **表名称：** 负库存提示配置-主表
- **表名：** t_im_negative_tip_cf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbaltb | 余额表标识 | varchar | 50 |  | √ | ' ' | 余额表 bal_balanceinfo |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fbillscope | 单据范围 | varchar | 512 |  | √ | ' ' | 单据范围,枚举: |
| 8 | fdesp | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 9 | fenable | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态,枚举: 0 :禁用 1 :启用 |
| 10 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_negative_tip_cf |  | fid |
| 2 | idx_negative_tip_fnumber |  | fnumber |

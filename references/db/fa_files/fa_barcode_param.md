# 资产条码启用参数-fa_barcode_param

## 资产类别-多选基础资料表 t_fa_barcode_mulcat

- **表名称：** 资产类别-多选基础资料表
- **表名：** t_fa_barcode_mulcat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_bc_mulcat_fdetail |  | fid |
| 2 | pk_t_fa_barcode_mulcat |  | fpkid |

---

## 资产条码启用参数-主表 t_fa_barcode_param

- **表名称：** 资产条码启用参数-主表
- **表名：** t_fa_barcode_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgentype | 条码生成方式 | bpchar | 1 |  | √ | '1' | 条码生成方式,枚举: 1 :全部资产卡片 2 :按资产类别启用 |
| 3 | fbarcoderuleid | 资产条码规则 | int8 | 64 |  | √ | 0 | [资产条码规则 barcm_barcoderule_fa](../barcm_files/barcm_barcoderule_fa.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_barcode_param |  | fid |
| 2 | idx_fa_bc_param_fruleid |  | fbarcoderuleid |

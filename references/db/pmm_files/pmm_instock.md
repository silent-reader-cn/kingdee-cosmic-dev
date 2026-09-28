# 库存调整-pmm_instock

## 库存调整-多语言表 t_mal_instock_l

- **表名称：** 库存调整-多语言表
- **表名：** t_mal_instock_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_instock_l_pkey |  | fpkid |
| 2 | idx_mal_instock_l_fid |  | fid,flocaleid |

---

## 库存调整-分表 t_mal_instock_a

- **表名称：** 库存调整-分表
- **表名：** t_mal_instock_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_instock_a_pkey |  | fid |
| 2 | idx_mal_instock_a_fcreatetime |  | fcreatetime |

---

## 库存调整-主表 t_mal_instock

- **表名称：** 库存调整-主表
- **表名：** t_mal_instock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 3 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 4 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :增加库存 2 :减少库存 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbilldate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 8 | fcontacterid | fcontacterid | int8 | 64 |  | √ | 0 |  |
| 9 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 10 | fbillno | 调整单号 | varchar | 80 |  | √ | ' ' | 调整单号 |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_instock_pkey |  | fid |
| 2 | idx_mal_instock_fbillno |  | fbillno |
| 3 | idx_mal_instock_fbilldate |  | fbilldate |
| 4 | idx_mal_instock_fbizpartnerid |  | fbizpartnerid |

---

## 商品明细分录-子表 t_mal_instockentry

- **表名称：** 商品明细分录-子表
- **表名：** t_mal_instockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 调整数量 | numeric | 19 | 6 | √ | 0.000000 | 调整数量 |
| 3 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品管理 pmm_prodmanage |
| 4 | fcurrentqty | 现有库存量 | numeric | 19 | 6 | √ | 0.000000 | 现有库存量 |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 10 | fnewqty | 调整后数量 | numeric | 19 | 6 | √ | 0.000000 | 调整后数量 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_instockentry_fgoodsid |  | fgoodsid |
| 2 | t_mal_instockentry_pkey |  | fentryid |
| 3 | idx_mal_instockentry_fid_fseq |  | fid,fseq |

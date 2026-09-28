# 上架申请-ent_prodrequest

## 上架申请-分表 t_mal_prodenter_a

- **表名称：** 上架申请-分表
- **表名：** t_mal_prodenter_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsuggestion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 审批时间 | timestamp | 0 |  |  | null | 审批时间 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcfmid | 审批人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_prodenter_a_pkey |  | fid |
| 2 | idx_mal_prodenter_a_ftime |  | fcreatetime |

---

## 上架申请-多语言表 t_mal_prodenter_l

- **表名称：** 上架申请-多语言表
- **表名：** t_mal_prodenter_l

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
| 1 | idx_mal_prodenter_l_fid |  | fid,flocaleid |
| 2 | t_mal_prodenter_l_pkey |  | fpkid |

---

## 商品分录-子表 t_mal_prodenterentry

- **表名称：** 商品分录-子表
- **表名：** t_mal_prodenterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshopprice | 商城价 | numeric | 23 | 10 | √ | 0.0000000000 | 商城价 |
| 3 | fentryresult | 审批结果 | bpchar | 1 |  | √ | ' ' | 审批结果,枚举: 1 :同意上架 0 :不同意上架 |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品管理 ent_prodmanage |
| 5 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_goodsclass |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 9 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 结算价 |
| 10 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodenter_fid_fseq |  | fid,fseq |
| 2 | idx_mal_prodenter_fgoodsid |  | fgoodsid |
| 3 | t_mal_prodenterentry_pkey |  | fentryid |

---

## 上架申请-主表 t_mal_prodenter

- **表名称：** 上架申请-主表
- **表名：** t_mal_prodenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 5 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 8 | fsupplierid | 商家 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fcfmstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :待审批 B :通过 C :部分通过 D :不通过 |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :上架 2 :下架 |
| 11 | fpersonid | 商家联系人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbillno | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 13 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodenter_fbilldate |  | fbilldate |
| 2 | idx_mal_prodenter_fbizid |  | fbizpartnerid |
| 3 | t_mal_prodenter_pkey |  | fid |
| 4 | idx_mal_prodenter_fbillno |  | fbillno |

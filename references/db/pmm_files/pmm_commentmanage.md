# 评价信息管理-pmm_commentmanage

## 评价信息管理-主表 t_mal_commentmanage

- **表名称：** 评价信息管理-主表
- **表名：** t_mal_commentmanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpictureurl | 图片列表 | varchar | 255 |  | √ | ' ' | 图片列表 |
| 3 | fprivacyprotectway | 匿名方式 | bpchar | 1 |  | √ | ' ' | 匿名方式,枚举: A :无匿名 B :半匿名 C :全匿名 |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 5 | fabandonuserid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 评价时间 | timestamp | 0 |  |  | null | 评价时间 |
| 7 | forderid | 订单编码 | int8 | 64 |  | √ | 0 | [商城订单 mal_order_bd](../mal_files/mal_order_bd.md) |
| 8 | fallowabandon | 允许评价人作废 | bpchar | 1 |  | √ | '1' | 允许评价人作废 |
| 9 | fcommenttype | 评价类型 | bpchar | 1 |  | √ | ' ' | 评价类型,枚举: 0 :初评 1 :追评 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [商城供应商 bd_malsupplier](../basedata_files/bd_malsupplier.md) |
| 12 | fabandondate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 13 | fstatus | 评价状态 | bpchar | 1 |  | √ | ' ' | 评价状态,枚举: A :暂存 B :已提交 C :已审核 D :已作废 |
| 14 | fcreatorid | 评价人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fpictureurl_tag | 图片列表_详情 | text | 0 |  |  | null | 图片列表_详情 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fabandonreason | 作废理由 | varchar | 512 |  | √ | ' ' | 作废理由 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_commentmge_forder |  | forderid |
| 2 | pk_t_mal_commentmanage |  | fid |
| 3 | idx_mal_commentmge_fgoods |  | fgoodsid |

---

## 评价信息-多语言表 t_mal_commentmanageentry_l

- **表名称：** 评价信息-多语言表
- **表名：** t_mal_commentmanageentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fcommenttitle | 标题 | varchar | 80 |  | √ | ' ' | 标题 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_commentmanageentry_l |  | fpkid |
| 2 | idx_mal_commgeentry_l_fid |  | fid,flocaleid |

---

## 评价信息-子表 t_mal_commentmanageentry

- **表名称：** 评价信息-子表
- **表名：** t_mal_commentmanageentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroup | fgroup | varchar | 80 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fmoduletype | 组件类型 | int8 | 64 |  | √ | 0 | [组件类型 pmm_moduletype](../pmm_files/pmm_moduletype.md) |
| 5 | fcontent | 评价内容 | varchar | 1000 |  | √ | ' ' | 评价内容 |
| 6 | fcommenttitle | 标题 | varchar | 80 |  | √ | ' ' | 标题 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_commgeent_fid_fseq |  | fid,fseq |
| 2 | pk_t_mal_commentmanageentry |  | fentryid |

# 资产重估单-fa_revaluation

## 重估详情-多语言表 t_fa_revaluationdetail_l

- **表名称：** 重估详情-多语言表
- **表名：** t_fa_revaluationdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_revaluationdetail_l |  | fpkid |
| 2 | idx_fa_revaluationd_l_id |  | fid,flocaleid |

---

## 重估详情-子表 t_fa_revaluationdetail

- **表名称：** 重估详情-子表
- **表名：** t_fa_revaluationdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdepreperiodeffect | 折旧影响期间 | varchar | 50 |  | √ | ' ' | 折旧影响期间,枚举: CUR :影响当期 NEXT :影响下期 |
| 5 | frevaluaterate | 重估率（%） | numeric | 19 | 6 | √ | 0 | 重估率（%） |
| 6 | frealcardbaseld | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 7 | frevaluationreserve | 重估准备金 | numeric | 19 | 6 | √ | 0 | 重估准备金 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fafteraccumdepre | 重估后累计折旧 | numeric | 19 | 6 | √ | 0 | 重估后累计折旧 |
| 10 | fpreoriginalval | 重估前资产原值 | numeric | 19 | 6 | √ | 0 | 重估前资产原值 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fpreaccumdepre | 重估前累计折旧 | numeric | 19 | 6 | √ | 0 | 重估前累计折旧 |
| 13 | frevaluatetype | 重估类型 | varchar | 50 |  | √ | ' ' | 重估类型,枚举: RRATE :按重估率重估 ORIGIN :按资产原值重估 |
| 14 | fafteroriginalval | 重估后资产原值 | numeric | 19 | 6 | √ | 0 | 重估后资产原值 |
| 15 | ffincardid | 财务卡片编码 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_revaluationde_id |  | fid |
| 2 | pk_fa_revaluationdetail |  | fentryid |

---

## 资产重估单-主表 t_fa_revaluation

- **表名称：** 资产重估单-主表
- **表名：** t_fa_revaluation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisamortize | 摊销重估准备 | bpchar | 1 |  | √ | '0' | 摊销重估准备 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fisdeprecate | 重估累计折旧 | bpchar | 1 |  | √ | '0' | 重估累计折旧 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fisscrap | 报废重估准备 | bpchar | 1 |  | √ | '0' | 报废重估准备 |
| 10 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fassetbookid | fassetbookid | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fxkpolicy | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 15 | frevaluatedate | 重估日期 | timestamp | 0 |  |  | null | 重估日期 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_revaluation_billno |  | fbillno |
| 2 | pk_fa_revaluation |  | fid |

---

## 资产重估单-多语言表 t_fa_revaluation_l

- **表名称：** 资产重估单-多语言表
- **表名：** t_fa_revaluation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_revaluation_l_cid |  | fid,flocaleid |
| 2 | pk_fa_revaluation_l |  | fpkid |

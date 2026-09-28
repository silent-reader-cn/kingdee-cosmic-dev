# 资产损失税前扣除台账-tccit_asset_loss_pre_tax

## 资产损失税前扣除台账-主表 t_tccit_asset_loss_pt

- **表名称：** 资产损失税前扣除台账-主表
- **表名：** t_tccit_asset_loss_pt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzcsszbjhx | 资产损失准备金核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产损失准备金核销金额 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fassetlosstype | 资产损失类型 | int8 | 64 |  | √ | 0 | 资产损失备查关系映射(树) tpo_assetlossmap_tree |
| 5 | fupstreambillno | 上游单据编号 | varchar | 50 |  | √ | ' ' | 上游单据编号 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fassetorigin | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | frecordtype | 备查类型 | varchar | 50 |  | √ | ' ' | 备查类型,枚举: 1 :专项申报 2 :清单申报 |
| 10 | fzcsyzzje | 资产损益账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产损益账载金额 |
| 11 | fcompensateincome | 赔偿收入 | numeric | 23 | 10 | √ | 0.0000000000 | 赔偿收入 |
| 12 | fsource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: handadd :手工新增 system :系统生成 import :数据引入 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcleanupdate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 16 | fcleanupincome | 清理收入 | numeric | 23 | 10 | √ | 0.0000000000 | 清理收入 |
| 17 | fcleanupfee | 清理费用 | numeric | 23 | 10 | √ | 0.0000000000 | 清理费用 |
| 18 | fjszjqc | 加速折旧类别 | varchar | 50 |  | √ | ' ' | 加速折旧类别 |
| 19 | fzctype | 会计资产类别 | varchar | 50 |  | √ | ' ' | 会计资产类别 |
| 20 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 21 | fdepreuseid | 上游单据折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fname | 资产名称 | varchar | 50 |  | √ | ' ' | 资产名称 |
| 24 | ffzcssjxzc | 非正常损失进项转出 | numeric | 23 | 10 | √ | 0.0000000000 | 非正常损失进项转出 |
| 25 | fbillstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 0 :禁用 1 :可用 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fzcsyssje | 资产损益税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 资产损益税收金额 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fljswzjtxe | 累计税务折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税务折旧摊销额 |
| 30 | fbaddebtdocno | 坏账损失单据编号 | varchar | 50 |  | √ | ' ' | 坏账损失单据编号 |
| 31 | fcleanupquantity | 清理数量 | numeric | 23 | 10 | √ | 0.0000000000 | 清理数量 |
| 32 | ftempdiffer | 暂时性差异 | bpchar | 1 |  | √ | ' ' | 暂时性差异 |
| 33 | fassetquantiy | 资产数量 | numeric | 23 | 10 | √ | 0.0000000000 | 资产数量 |
| 34 | fljjszjtxe | 累计实际折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计实际折旧摊销额 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | fassetno | 资产编码 | int8 | 64 |  | √ | 0 | [资产清单 tdm_asset_data](../tdm_files/tdm_asset_data.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_asset_loss_pt |  | fid |
| 2 | idx_tccit_asset_loss_pt |  | fbillno |

---

## 资产编码废弃-多选基础资料表 t_tccit_asset_loss_pt_b

- **表名称：** 资产编码废弃-多选基础资料表
- **表名：** t_tccit_asset_loss_pt_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [汇缴资产折旧摊销台账（废弃） tccit_hjzczjtx_account](../tccit_files/tccit_hjzczjtx_account.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_asset_loss_pt_b_fk |  | fid |
| 2 | pk_tccit_asset_loss_pt_b |  | fpkid |

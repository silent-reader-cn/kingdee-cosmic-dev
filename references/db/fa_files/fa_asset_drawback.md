# 资产退库单-fa_asset_drawback

## 资产退库单实物分录-子表 t_fa_assetdrawback_entry

- **表名称：** 资产退库单实物分录-子表
- **表名：** t_fa_assetdrawback_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimstorekeeper | 库管员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstoreplaceid | fstoreplaceid | int8 | 64 |  | √ | 0 |  |
| 4 | fcomment | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 5 | fdrawstoreplace | 退库存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | [使用状态 fa_usestatus](../fa_files/fa_usestatus.md) |
| 8 | famount | 资产数量 | numeric | 19 | 6 | √ | 0.000000 | 资产数量 |
| 9 | fcardstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 10 | fdrawusestatus | 退库使用状态 | int8 | 64 |  | √ | 0 | [使用状态 fa_usestatus](../fa_files/fa_usestatus.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | frealcardid | 资产名称 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetdrawback_entry_pkey |  | fentryid |
| 2 | idx_fa_assdra_ent_fid |  | fid |

---

## 资产退库单-主表 t_fa_assetdrawback

- **表名称：** 资产退库单-主表
- **表名：** t_fa_assetdrawback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapplydate | 退库日期 | timestamp | 0 |  |  | null | 退库日期 |
| 4 | fappliertelephone | fappliertelephone | varchar | 30 |  | √ | ' ' |  |
| 5 | fassetorgid | 退库人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foperatorid | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :废弃 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fsigningdate | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 10 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :暂存 B :已提交 C :已签收 |
| 12 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 13 | freason | 申请事由 | varchar | 255 |  |  | ' ' | 申请事由 |
| 14 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 15 | frealassetorgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fapplierid | 退库人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsignerid | 组织库管员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fstoreplaceid | fstoreplaceid | int8 | 64 |  | √ | 0 |  |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fsourcetype | 来源方式 | varchar | 30 |  | √ | ' ' | 来源方式,枚举: 1 :移动端移交或领用 2 :手工新增 |
| 22 | fapplierdeptid | 退库人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetdrawback_pkey |  | fid |
| 2 | idx_fa_assdra_fbillno |  | fbillno |

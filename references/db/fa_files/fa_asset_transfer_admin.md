# 资产移交单-fa_asset_transfer_admin

## 资产转移单实物分录-子表 t_fa_assettransfer_entry

- **表名称：** 资产转移单实物分录-子表
- **表名：** t_fa_assettransfer_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftransusestatus | 使用状态 | int8 | 64 |  | √ | 0 | [使用状态 fa_usestatus](../fa_files/fa_usestatus.md) |
| 3 | fstoreplaceid | fstoreplaceid | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 资产数量 | numeric | 19 | 6 | √ | 0.000000 | 资产数量 |
| 6 | fcardstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 7 | ftransstoreplace | 接收存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | frealcardid | 资产名称 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assettransfer_entry_pkey |  | fentryid |
| 2 | idx_fa_asstra_ent_fid |  | fid |

---

## 资产移交单-主表 t_fa_assettransfer

- **表名称：** 资产移交单-主表
- **表名：** t_fa_assettransfer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassetorgid | fassetorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fappliertelephone | fappliertelephone | varchar | 30 |  | √ | ' ' |  |
| 4 | forgid | 移交人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :暂存 B :已提交 C :已签收 |
| 6 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 7 | freceiverorgid | 接收人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsenderid | 移交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fstoreplaceid | 接收存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | freceiveassetorgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fsourcetype | 来源方式 | varchar | 30 |  | √ | ' ' | 来源方式,枚举: 1 :移动端移交或领用 2 :手工新增 |
| 14 | fapplierdeptid | fapplierdeptid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fapplydate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :废弃 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | freceivertelephone | freceivertelephone | varchar | 30 |  | √ | ' ' |  |
| 21 | fsigningdate | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 22 | freceiverid | 接收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | freason | 申请事由 | varchar | 255 |  | √ | ' ' | 申请事由 |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fsignerid | 签收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_asstra_fbillno |  | fbillno |
| 2 | t_fa_assettransfer_pkey |  | fid |

# 印花税应税凭证-tdm_stamptax_voucher

## 印花税应税凭证-主表 t_tdm_stamptax_voucher

- **表名称：** 印花税应税凭证-主表
- **表名：** t_tdm_stamptax_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 应纳税凭证种类 | varchar | 50 |  | √ | ' ' | 应纳税凭证种类,枚举: 12 :技术合同 13 :融资租赁合同 14 :买卖合同 15 :承揽合同 16 :建设工程合同 17 :运输合同 18 :借款合同 19 :租赁合同 20 :保管合同 21 :仓储合同 22 :财产保险合同 23 :土地使用权出让书据 24 :土地使用权、房屋等建筑物和构筑物所有权转让书据（不包括土地承包经营权和土地经营权转移） 25 :股权转让书据（不包括应缴纳证券交易印花税的） 26 :商标专用权、著作权、专利权、专有技术使用权使用权转让书据 27 :营业账簿 1 :购销合同 2 :加工承揽合同 3 :建设工程勘察设计合同 4 :建筑安装工程承包合同 5 :财产租赁合同 6 :货物运输合同 7 :仓储保管合同 8 :借款合同 9 :财产保险合同 10 :技术合同 11 :产权转移书据 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsigndate | 签约日期 | timestamp | 0 |  |  | null | 签约日期 |
| 5 | fvouchercode | 应税凭证编号 | varchar | 50 |  | √ | ' ' | 应税凭证编号 |
| 6 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexcludetaxcount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fvouchername | 应税凭证名称 | varchar | 50 |  | √ | ' ' | 应税凭证名称 |
| 11 | fsignatorydate | fsignatorydate | varchar | 50 |  | √ | ' ' |  |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | ftaxmoneyperiod | 税款属期 | timestamp | 0 |  |  | null | 税款属期 |
| 14 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsubvouchertype | 应税凭证子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fbuyer | 采购方 | varchar | 50 |  | √ | ' ' | 采购方 |
| 20 | fincludetaxcount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fvouchermoney | 应税凭证金额 | numeric | 23 | 10 | √ | 0 | 应税凭证金额 |
| 23 | fvouchertypeid | 应税凭证种类 | int8 | 64 |  | √ | 0 | 印花税税率（树） tpo_tcsd_taxrateentrytree |
| 24 | fsaler | 销售方 | varchar | 50 |  | √ | ' ' | 销售方 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_stamptax_voucher_pkey |  | fid |
| 2 | idx_tdm_stamptax_voucher |  | fvouchercode |

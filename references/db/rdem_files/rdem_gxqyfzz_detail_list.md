# 高新企业明细台账(废弃)-rdem_gxqyfzz_detail_list

## 高新企业明细台账(废弃)-主表 t_rdem_fzzmx_gx_yft

- **表名称：** 高新企业明细台账(废弃)-主表
- **表名：** t_rdem_fzzmx_gx_yft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 记账凭证类型 | varchar | 50 |  | √ | ' ' | 记账凭证类型 |
| 3 | fdebitlocalcurrency | 借方本币金额 | numeric | 23 | 2 | √ | 0 | 借方本币金额 |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fvouchercode | 记账凭证编号 | varchar | 50 |  | √ | ' ' | 记账凭证编号 |
| 8 | fvoucherdate | 记账凭证日期 | timestamp | 0 |  |  | null | 记账凭证日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fgjysz | 归集要素值 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fgjyslx | 归集要素类型 | varchar | 50 |  | √ | ' ' | 归集要素类型,枚举: bos_costcenter :成本中心 bd_project :项目 |
| 16 | fvoucherremark | 记账凭证摘要 | varchar | 2000 |  | √ | ' ' | 记账凭证摘要 |
| 17 | fyfxmxx | 研发项目 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 18 | fbalancelocalcurrency | 本币发生金额 | numeric | 23 | 2 | √ | 0 | 本币发生金额 |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 23 | fcreditlocalcurrency | 贷方本币金额 | numeric | 23 | 2 | √ | 0 | 贷方本币金额 |
| 24 | fsbxm | 申报项目 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 25 | fbalanceid | 科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 26 | fisvalid | fisvalid | bpchar | 1 |  | √ | '0' |  |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fcost | 费用类型 | int8 | 64 |  | √ | 0 | [高新费用类别 rdem_high_tech_costtype](../rdem_files/rdem_high_tech_costtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_fzzmx_gx_yft_m0 |  | fbillno |
| 2 | pk_rdem_fzzmx_gx_yft |  | fid |

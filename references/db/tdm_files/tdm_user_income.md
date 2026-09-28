# 人员收入信息-tdm_user_income

## 人员收入信息-主表 t_tdm_user_income

- **表名称：** 人员收入信息-主表
- **表名：** t_tdm_user_income

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fproject | 所得项目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tiit_bizdef_entry |
| 12 | fbillno | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_user_income |  | fid |
| 2 | idx_tdm_user_income |  | fbillno |

---

## 明细行-子表 t_detailentry

- **表名称：** 明细行-子表
- **表名：** t_detailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcardno | 证件号码 | varchar | 50 |  | √ | ' ' | 证件号码 |
| 3 | fthreesyxyyezh | 累计3岁以下婴幼儿照护 | numeric | 23 | 10 | √ | 0 | 累计3岁以下婴幼儿照护 |
| 4 | fljsylr | 累计赡养老人 | numeric | 23 | 10 | √ | 0 | 累计赡养老人 |
| 5 | fqnycxjje | 全年一次性奖金额 | numeric | 23 | 10 | √ | 0 | 全年一次性奖金额 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fyssr | 本期收入 | numeric | 23 | 10 | √ | 0 | 本期收入 |
| 8 | fjbyilbxf | 基本医疗保险费 | numeric | 23 | 10 | √ | 0 | 基本医疗保险费 |
| 9 | fother | 其他扣除 | numeric | 23 | 10 | √ | 0 | 其他扣除 |
| 10 | fnotes | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 11 | fjxjy | 累计继续教育 | numeric | 23 | 10 | √ | 0 | 累计继续教育 |
| 12 | fpaidalreadyamount | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 13 | fpayable | 应纳税所得额 | numeric | 23 | 10 | √ | 0 | 应纳税所得额 |
| 14 | fzfzj | 累计住房租金 | numeric | 23 | 10 | √ | 0 | 累计住房租金 |
| 15 | frate | 税率/扣除率 | numeric | 23 | 10 | √ | 0 | 税率/扣除率 |
| 16 | fretaxamount | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 17 | fjbylbxf | 基本养老保险费 | numeric | 23 | 10 | √ | 0 | 基本养老保险费 |
| 18 | ftaxrefundamount | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 19 | fbqmssrhj | 本期免税收入 | numeric | 23 | 10 | √ | 0 | 本期免税收入 |
| 20 | ftaxdeferral | 税延养老保险 | numeric | 23 | 10 | √ | 0 | 税延养老保险 |
| 21 | fsybxf | 失业保险费 | numeric | 23 | 10 | √ | 0 | 失业保险费 |
| 22 | freduction | 减免项目代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 23 | fzfgjj | 住房公积金 | numeric | 23 | 10 | √ | 0 | 住房公积金 |
| 24 | fname | 姓名 | int8 | 64 |  | √ | 0 | [人员基础信息 tdm_userbaseinfo](../tdm_files/tdm_userbaseinfo.md) |
| 25 | faccumulaterecost | 累计减除费用 | numeric | 23 | 10 | √ | 0 | 累计减除费用 |
| 26 | frecost | 减除费用 | numeric | 23 | 10 | √ | 0 | 减除费用 |
| 27 | fworkno | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
| 28 | fcardtype | 证件类型 | varchar | 50 |  | √ | ' ' | 证件类型,枚举: 1 :居民身份证 2 :中国护照 3 :港澳居民来往内地通行证 4 :台湾居民来往大陆通行证 5 :港澳居民居住证 6 :台湾居民居住证 7 :外国护照 8 :外国人永久居留身份证 9 :外国人工作许可证(A类) 10 :外国人工作许可证(B类) 11 :外国人工作许可证(C类) |
| 29 | ftaxreductionratio | 减税计税比例 | numeric | 23 | 10 | √ | 0 | 减税计税比例 |
| 30 | fotherdeduct | fotherdeduct | numeric | 23 | 10 | √ | 0 |  |
| 31 | fproperty | 财产原值 | numeric | 23 | 10 | √ | 0 | 财产原值 |
| 32 | fgrylj | 累计个人养老金 | numeric | 23 | 10 | √ | 0 | 累计个人养老金 |
| 33 | fpayabletaxamount | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 34 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 35 | fljzfdklx | 累计住房贷款利息 | numeric | 23 | 10 | √ | 0 | 累计住房贷款利息 |
| 36 | fzykcdjze | 准予扣除的捐赠额 | numeric | 23 | 10 | √ | 0 | 准予扣除的捐赠额 |
| 37 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 38 | fhealthinsurance | 商业健康保险 | numeric | 23 | 10 | √ | 0 | 商业健康保险 |
| 39 | fljznjy | 累计子女教育 | numeric | 23 | 10 | √ | 0 | 累计子女教育 |
| 40 | fallowdeduct | 允许扣除的税费 | numeric | 23 | 10 | √ | 0 | 允许扣除的税费 |
| 41 | fdeduct | 速算扣除数 | int8 | 64 |  | √ | 0 | 速算扣除数 |
| 42 | faccumulatespecial | 累计专项扣除 | numeric | 23 | 10 | √ | 0 | 累计专项扣除 |
| 43 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 44 | fannuity | 企业（职业）年金 | numeric | 23 | 10 | √ | 0 | 企业（职业）年金 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fcost | 本期费用 | numeric | 23 | 10 | √ | 0 | 本期费用 |
| 47 | faccumulateincome | 累计收入额 | numeric | 23 | 10 | √ | 0 | 累计收入额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_detailentry |  | fentryid |
| 2 | idx_detailentry_fk |  | fid |

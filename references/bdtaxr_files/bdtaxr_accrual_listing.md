# 应计提清单-bdtaxr_accrual_listing

## 应计提清单-主表 t_bdtaxr_accrual_listing

- **表名称：** 应计提清单-主表
- **表名：** t_bdtaxr_accrual_listing

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcategory | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型,枚举: zzs :增值税计提底稿 qysdsjb :企业所得税预缴计提底稿 sdsjt_bd :递延所得税计提底稿（本地） sdsjt_jt :递延所得税计提底稿（集团） yhs :印花税计提底稿 fcs :房产税计提底稿 cztdsys :城镇土地使用税计提底稿 hjbhs :环保税计提底稿 ccs :车船税计提底稿 szys :水资源税计提底稿 |
| 3 | fbillstatus | 计提底稿状态 | varchar | 50 |  | √ | ' ' | 计提底稿状态,枚举: A :暂存 B :已提交 C :已审核 noneed :无需编制 nodata :未编制 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | faccountsettype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型,枚举: bdzt :本地账簿 jtzt :集团账簿 |
| 6 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 7 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 10 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 11 | fmonth | 生成年月 | timestamp | 0 |  |  | null | 生成年月 |
| 12 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 13 | fbillno | 计提底稿编号 | varchar | 50 |  | √ | ' ' | 计提底稿编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_accrual_listing |  | fid |
| 2 | idx_bdtaxr_accrual_listing_0 |  | forgid,ftaxsystem,ftaxareagroup,ftaxtype,fcategory |

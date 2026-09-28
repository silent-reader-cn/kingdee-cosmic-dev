# 申报检查-tsate_declare_checklist

## 申报检查-主表 t_tsate_checklist

- **表名称：** 申报检查-主表
- **表名：** t_tsate_checklist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzsxm | 征收项目 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 5 | fsbsx | 申报事项 | varchar | 50 |  | √ | ' ' | 申报事项 |
| 6 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 7 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 8 | fsbqx | 申报期限 | timestamp | 0 |  |  | null | 申报期限 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 11 | fsjly | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :税局下载 2 :手工导入 |
| 12 | funiquecode | 唯一标识 | varchar | 50 |  | √ | ' ' | 唯一标识 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fgxsj | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 15 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 19 | fswjgmc | 税务机关名称（特殊） | varchar | 50 |  | √ | ' ' | 税务机关名称（特殊） |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 22 | fjkzt | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: 2 :无需缴款 0 :未缴款 1 :已缴款 |
| 23 | ftaxorgid | 主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 24 | fsbzt | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: 0 :未申报 1 :已申报 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_checklist |  | fid |
| 2 | idx_tsate_check_nsr |  | fskssqq,fskssqz,fnsrsbh |

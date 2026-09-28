# 项目装箱单F7-mpm_proencasement_f7

## 项目装箱单F7-主表 t_mpm_proencase

- **表名称：** 项目装箱单F7-主表
- **表名：** t_mpm_proencase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpackmanagerid | 点收负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fboxnum | 箱号 | varchar | 50 |  | √ | ' ' | 箱号 |
| 5 | fgroupnumid | 组号 | int8 | 64 |  | √ | 0 | [组号 mpm_groupnumber](../mpm_files/mpm_groupnumber.md) |
| 6 | fpacksupplierid | 包装供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | ftransvehibrand | 运输工具牌号 | varchar | 255 |  | √ | ' ' | 运输工具牌号 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fprojectheadid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 11 | fcontainernum | 集装箱号 | varchar | 255 |  | √ | ' ' | 集装箱号 |
| 12 | flogcontper | 物流联系人 | varchar | 255 |  | √ | ' ' | 物流联系人 |
| 13 | fboxcode | fboxcode | varchar | 255 |  | √ | ' ' |  |
| 14 | flogcompanyid | 物流公司 | int8 | 64 |  | √ | 0 | [物流公司 pur_logsupplier](../pbd_files/pur_logsupplier.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 20 | flogtracknum | 物流单号 | varchar | 255 |  | √ | ' ' | 物流单号 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fpackdate | 装箱日期 | timestamp | 0 |  |  | null | 装箱日期 |
| 23 | flogcontphone | 物流联系电话 | varchar | 50 |  | √ | ' ' | 物流联系电话 |
| 24 | fgrouprelid | 组号序号关联关系 | int8 | 64 |  | √ | 0 | [项目装箱单组号关联关系 mpm_encasegrouprel](../mpm_files/mpm_encasegrouprel.md) |
| 25 | flogistics | flogistics | bpchar | 1 |  | √ | '0' |  |
| 26 | fexternalnum | fexternalnum | varchar | 100 |  | √ | ' ' |  |
| 27 | fpointstatus | fpointstatus | bpchar | 1 |  | √ | 'A' |  |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_proencase |  | fid |
| 2 | idx_mpm_proencase_bno |  | fbillno |

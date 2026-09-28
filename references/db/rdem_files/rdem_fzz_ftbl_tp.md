# 辅助账分摊比例（临时表）-rdem_fzz_ftbl_tp

## 辅助账分摊比例（临时表）-主表 t_rdem_fzz_ftbl_tp

- **表名称：** 辅助账分摊比例（临时表）-主表
- **表名：** t_rdem_fzz_ftbl_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostcenterid | 成本中心名称 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fshareratio | 分摊比例 | numeric | 23 | 10 | √ | 0 | 分摊比例 |
| 4 | fgatherendtime | 截止月份 | int8 | 64 |  | √ | 0 | 截止月份 |
| 5 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fweightsum | 权重汇总 | numeric | 23 | 2 | √ | 0 | 权重汇总 |
| 7 | fpaytype | 支出类型 | varchar | 50 |  | √ | ' ' | 支出类型,枚举: capital :资本化 cost :费用化 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fftrule | 分摊配置单据体的id | varchar | 2000 |  | √ | ' ' | 分摊配置单据体的id |
| 11 | fweight | 权重 | numeric | 23 | 2 | √ | 0 | 权重 |
| 12 | fdevprojectid | 项目编号 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 13 | fpersonno | 人员工号 | varchar | 50 |  | √ | ' ' | 人员工号 |
| 14 | fgroupdime | 分组维度 | varchar | 50 |  | √ | ' ' | 分组维度,枚举: taxorg :税务组织 costcenter :成本中心 staffnumber :人员工号 |
| 15 | fgroupkey | 分摊组合 | varchar | 50 |  | √ | ' ' | 分摊组合 |
| 16 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 17 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 18 | fmonth | 月份 | int8 | 64 |  | √ | 0 | 月份 |
| 19 | fpersonname | 人员名称 | varchar | 50 |  | √ | ' ' | 人员名称 |
| 20 | fsbxm | 申报项目 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 21 | fsharetypeid | 分摊类型 | int8 | 64 |  | √ | 0 | [分摊类型 rdem_share_type](../rdem_files/rdem_share_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_fzz_ftbl_tp_m0 |  | fgatherendtime |
| 2 | pk_rdem_fzz_ftbl_tp |  | fid |

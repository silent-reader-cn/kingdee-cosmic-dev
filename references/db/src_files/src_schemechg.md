# 推荐方案变更-src_schemechg

## 推荐方案变更-主表 t_src_schemechg

- **表名称：** 推荐方案变更-主表
- **表名：** t_src_schemechg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fschemeid | 推荐方案(变更前) | int8 | 64 |  | √ | 0 | 推荐方案 src_pattern |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fwinruleid | 中标原则(变更前) | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 9 | fnewruleassess | 商务报价计算规则（招标）(变更后) | bpchar | 1 |  | √ | ' ' | 商务报价计算规则（招标）(变更后),枚举: 1 :标的单价 2 :报价包的采购总金额 3 :报价包内所有产品的平均价 4 :其他 |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 11 | fvietype | 竞价类型(变更前) | bpchar | 1 |  | √ | ' ' | 竞价类型(变更前),枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 12 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 13 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 14 | fnewwinruleid | 中标原则(变更后) | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 15 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 16 | fruleassess | 商务报价计算规则（招标）(变更前) | bpchar | 1 |  | √ | ' ' | 商务报价计算规则（招标）(变更前),枚举: 1 :标的单价 2 :报价包的采购总金额 3 :报价包内所有产品的平均价 4 :其他 |
| 17 | fnewvietype | 竞价类型(变更后) | bpchar | 1 |  | √ | ' ' | 竞价类型(变更后),枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 18 | fnewschemeid | 推荐方案(变更后) | int8 | 64 |  | √ | 0 | 推荐方案 src_pattern |
| 19 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_schemechg_pid |  | fparentid |
| 2 | pk_src_schemechg |  | fid |

# 发票领购详情-sim_inv_apply_detail

## 发票领购详情-主表 t_sim_inv_apply_detail

- **表名称：** 发票领购详情-主表
- **表名：** t_sim_inv_apply_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 3 | fdealtime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 4 | fsycnid | 同步id | varchar | 50 |  | √ | ' ' | 同步id |
| 5 | finvoicequantity | 发票份数 | int8 | 64 |  | √ | 0 | 发票份数 |
| 6 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fapplystate | 申领类型 | varchar | 30 |  | √ | ' ' | 申领类型,枚举: 0 :新建 1 :重试 |
| 8 | fdealwithtime | 征管处理时间 | timestamp | 0 |  |  | null | 征管处理时间 |
| 9 | fagent | 经办人 | varchar | 25 |  | √ | ' ' | 经办人 |
| 10 | fresultaskflag | 结果查询标记 | varchar | 4 |  | √ | ' ' | 结果查询标记,枚举: 0 :未处理 1 :申领已处理 2 :领购已处理 3 :已分发 |
| 11 | fstartnumber | 起始号码 | varchar | 30 |  | √ | ' ' | 起始号码 |
| 12 | forg | 组织 | int8 | 64 |  | √ | 0 | 企业管理 bdm_org |
| 13 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | 企业基础信息 bdm_enterprise_baseinfo |
| 14 | fconductor | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fpreappnumber | 预申请编号 | varchar | 30 |  | √ | ' ' | 预申请编号 |
| 16 | fendnumber | 终止号码 | varchar | 30 |  | √ | ' ' | 终止号码 |
| 17 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 026 :普通电子发票 027 :专用电子发票 |
| 18 | fapplypurchasequantity | 领购数量 | int8 | 64 |  | √ | 0 | 领购数量 |
| 19 | fdealstate | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: 0 :申领中 1 :领购成功 2 :领购失败 -1 :撤销领购 |
| 20 | finvoicecode | 发票类型代码 | varchar | 30 |  | √ | ' ' | 发票类型代码 |
| 21 | fdealmessage | 征管处理信息 | varchar | 200 |  | √ | ' ' | 征管处理信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_inv_apply_detail |  | fepinfo,finvoicetype |
| 2 | pk_sim_inv_apply_detail |  | fid |

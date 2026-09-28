# 风险事件-rsa_riskevent

## 风险事件-主表 t_rsa_riskevent

- **表名称：** 风险事件-主表
- **表名：** t_rsa_riskevent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | frisklevelid | 风险等级 | int8 | 64 |  | √ | 0 | [风险等级 rsa_risklevel](../rsa_files/rsa_risklevel.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 事件状态 | bpchar | 1 |  | √ | ' ' | 事件状态,枚举: 0 :未处理 1 :已处理 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fnumericalunit | 指标数值单位 | bpchar | 1 |  | √ | ' ' | 指标数值单位 |
| 8 | fotherdimensionvalue_tag | 其他维度和值_详情 | text | 0 |  |  | null | 其他维度和值_详情 |
| 9 | frang | 风险等级值范围 | varchar | 50 |  | √ | ' ' | 风险等级值范围 |
| 10 | fbillno | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 11 | fremark | 处理备注 | varchar | 255 |  | √ | ' ' | 处理备注 |
| 12 | fotherdimensionvalue | 其他维度和值 | varchar | 251 |  | √ | ' ' | 其他维度和值 |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 分析期间 pa_analysisperiod |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | friskitemid | 风险检查项 | int8 | 64 |  | √ | 0 | [风险检查项 rsa_riskitem](../rsa_files/rsa_riskitem.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | ftimetype | 时间类型 | varchar | 50 |  | √ | ' ' | 时间类型,枚举: pa_analysisperiod :分析期间 bd_period :会计期间 |
| 21 | ffasindexid | 指标 | int8 | 64 |  | √ | 0 | [指标 pa_fasindex](../pa_files/pa_fasindex.md) |
| 22 | fvalue | 指标值 | numeric | 23 | 10 | √ | 0 | 指标值 |
| 23 | finfluence | 影响说明 | varchar | 255 |  | √ | ' ' | 影响说明 |
| 24 | fsendstatus | 发送消息 | bpchar | 1 |  | √ | ' ' | 发送消息,枚举: 0 :未发送 1 :已发送 |
| 25 | fchecktime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rsa_riskevent |  | forgid,fperiodid |
| 2 | idx_rsa_riskevent_search |  | fbillno |
| 3 | pk_t_rsa_riskevent |  | fid |

---

## 通知用户列表-多选基础资料表 t_rsa_noticeuser

- **表名称：** 通知用户列表-多选基础资料表
- **表名：** t_rsa_noticeuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rsa_noticeuser |  | fid |
| 2 | pk_t_rsa_noticeuser |  | fpkid |

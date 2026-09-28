# 银企日志-be_banklog

## 银企日志-主表 t_be_banklog

- **表名称：** 银企日志-主表
- **表名：** t_be_banklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 3 | fexceptionmsg | 异常原因 | varchar | 200 |  |  | null | 异常原因 |
| 4 | fpayacntid | 银行账户 | varchar | 100 |  | √ | ' ' | 银行账户 |
| 5 | fsendexceptioninfo_tag | 发送异常信息_详情 | text | 0 |  |  | null | 发送异常信息_详情 |
| 6 | fsourcebilltype | 业务单据 | varchar | 30 |  | √ | ' ' | 业务单据,枚举: be_bankagentpay :银行代发单 be_bankpaying :银行付款单 cas_betransdetail :交易明细 |
| 7 | fbanklogtype | 执行操作 | varchar | 30 |  | √ | ' ' | 执行操作,枚举: balance :查询账户余额 detail :下载交易明细 pay :提交银企付款 receipt :下载电子回单 updatePayStatus :修改付款状态 syncAccount :同步银行账户 listBankLogin :查询登陆信息 batchBalance :批量查询余额 queryPay :同步单据状态 |
| 8 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsourceid | 单据ID（兼容保留） | varchar | 100 |  | √ | ' ' | 单据ID（兼容保留） |
| 10 | fbankinterfaceid | 银行接口ID | varchar | 100 |  | √ | ' ' | 银行接口ID |
| 11 | fsendinfo_tag | 发送日志_详情 | text | 0 |  |  | null | 发送日志_详情 |
| 12 | freceiveexceptioninfo_tag | freceiveexceptioninfo_tag | text | 0 |  |  | null |  |
| 13 | ftranstype | 传输类型 | varchar | 30 |  | √ | ' ' | 传输类型,枚举: send :发送 Receiver :接收 exceptionSend :发送异常 exceptionReceive :接收类型 |
| 14 | fsendinfo | 发送日志 | text | 0 |  |  | null | 发送日志 |
| 15 | freceiveexceptioninfo | 接收异常信息 | text | 0 |  |  | null | 接收异常信息 |
| 16 | fqueryacntid | fqueryacntid | varchar | 100 |  | √ | ' ' |  |
| 17 | fbankinterface | 银行接口信息 | varchar | 100 |  | √ | ' ' | 银行接口信息 |
| 18 | fsendexceptioninfo | 发送异常信息 | text | 0 |  |  | null | 发送异常信息 |
| 19 | freceiveinfo | 接收信息 | text | 0 |  |  | null | 接收信息 |
| 20 | freceiveinfo_tag | 接收信息_详情 | text | 0 |  |  | null | 接收信息_详情 |
| 21 | fisexception | 执行结果 | bpchar | 1 |  | √ | ' ' | 执行结果,枚举: 0 :成功 1 :失败 |
| 22 | fsourcebillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 23 | fpayeeacntid | 收款账户 | varchar | 100 |  | √ | ' ' | 收款账户 |
| 24 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_banklog_pkey |  | fid |
| 2 | idx_be_blog_fsid |  | fsourceid |

---

## 关联子实体-子表 t_be_banklog_lk

- **表名称：** 关联子实体-子表
- **表名：** t_be_banklog_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_banklog_lk_pkey |  | fpkid |

---

## 银企日志-关联追踪表 t_be_banklog_tc

- **表名称：** 银企日志-关联追踪表
- **表名：** t_be_banklog_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_be_banklog_tc_tid |  | ftid |
| 2 | idx_be_banklog_tc_tbill |  | ftbillid |
| 3 | t_be_banklog_tc_pkey |  | fid |

---

## 银企日志-反写记录表 t_be_banklog_wb

- **表名称：** 银企日志-反写记录表
- **表名：** t_be_banklog_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_banklog_wb_pkey |  | fentryid |

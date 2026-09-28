# 银行付款响应码-aqap_bank_pay_rspcode

## 银行付款响应码-多语言表 t_aqap_pay_rsp_code_l

- **表名称：** 银行付款响应码-多语言表
- **表名：** t_aqap_pay_rsp_code_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_pay_rsp_code_l |  | fpkid |
| 2 | idx_aqap_pay_rsp_code_l |  | fid |

---

## 单据体-子表 t_aqap_pay_rsp

- **表名称：** 单据体-子表
- **表名：** t_aqap_pay_rsp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fout_rsp_parse | 银行外层响应码解析 | varchar | 255 |  |  | null | 银行外层响应码解析 |
| 3 | fseq | 分录行号 | int4 | 32 |  |  | null | 分录行号 |
| 4 | fin_rsp_parse | 银行内层响应码解析 | varchar | 255 |  |  | null | 银行内层响应码解析 |
| 5 | fproxy_rspmsg | 代理程序响应码释义 | varchar | 100 |  |  | null | 代理程序响应码释义 |
| 6 | fproxy_rspcode | 代理程序代码响应码 | varchar | 50 |  |  | null | 代理程序代码响应码 |
| 7 | fout_rspmsg | 外层响应码释义 | varchar | 100 |  |  | null | 外层响应码释义 |
| 8 | fin_rspmsg | 内层响应码释义 | varchar | 100 |  |  | null | 内层响应码释义 |
| 9 | finterface_name | 银行接口名称 | varchar | 50 |  | √ | ' ' | 银行接口名称 |
| 10 | fproxy_rsp_parse | 代理程序响应码解析 | varchar | 255 |  |  | null | 代理程序响应码解析 |
| 11 | fout_rspcode | 银行外层代码响应码 | varchar | 50 |  |  | null | 银行外层代码响应码 |
| 12 | fin_rspcode | 银行内层代码响应码 | varchar | 50 |  |  | null | 银行内层代码响应码 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | feb_status | 银企云付款状态 | varchar | 50 |  |  | null | 银企云付款状态,枚举: 交易成功 :交易成功 交易失败 :交易失败 交易未确认 :交易未确认 银行处理中 :银行处理中 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_pay_rsp |  | fid |
| 2 | pk_t_aqap_pay_rsp |  | fentryid |

---

## 银行付款响应码-主表 t_aqap_pay_rsp_code

- **表名称：** 银行付款响应码-主表
- **表名：** t_aqap_pay_rsp_code

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fgroupid | 银行版本 | int8 | 64 |  | √ | 0 | 银行启用管理 aqap_bank |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  |  | ' ' | 编码 |
| 11 | finterface | 银行接口名称 | int8 | 64 |  | √ | 0 | 银行接口维护 aqap_pay_interface |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_pay_rsp_code |  | fid |
| 2 | idx_aqap_pay_rsp_code |  | fgroupid |

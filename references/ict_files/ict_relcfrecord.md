# 现金流量数据-ict_relcfrecord

## 现金流量数据-主表 t_ict_relcfrecord

- **表名称：** 现金流量数据-主表
- **表名：** t_ict_relcfrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 凭证类型 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 3 | forgid | 本方核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbaldc | 余额方向（金额方向*现金流量项目方向） | varchar | 2 |  | √ | '1' | 余额方向（金额方向*现金流量项目方向）,枚举: 1 :现金流入 -1 :现金流出 |
| 5 | foriperiodid | 期间(原始) | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | fschemeid | 对账方案 | int8 | 64 |  | √ | 0 | 内部交易对账方案 ict_verifyscheme |
| 7 | fvoucherentry | 凭证分录ID | int8 | 64 |  | √ | 0 | 凭证分录ID |
| 8 | fcommonassgrp | 共同核算维度 | varchar | 500 |  | √ | ' ' | 共同核算维度 |
| 9 | famt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fstatus | 勾稽状态 | varchar | 10 |  | √ | ' ' | 勾稽状态,枚举: 0 :未勾稽 1 :部分勾稽 2 :完全勾稽 999 :单边勾稽 |
| 11 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 12 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | '0' | 来源类型,枚举: 0 :手工凭证 1 :结转损益 2 :期末调汇 3 :模式凭证 4 :机制凭证 5 :凭证摊销 6 :自动转账 7 :扫描生成 8 :外部导入 a :账簿协同 b :凭证对照 |
| 13 | fisnextperiod | 转入下期 | bpchar | 1 |  | √ | '0' | 转入下期 |
| 14 | famtbal | 余额 | numeric | 23 | 10 | √ | 0 | 余额 |
| 15 | fedescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 16 | fcashflowitemid | 现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 17 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fvoucherid | 凭证内码 | int8 | 64 |  | √ | 0 | 凭证内码 |
| 19 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 20 | foporgid | 对方核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 22 | fdc | 现金流向 | varchar | 10 |  | √ | ' ' | 现金流向,枚举: b :流入流出 i :现金流入 o :现金流出 |
| 23 | fbillstatus | 业务状态 | bpchar | 1 |  | √ | 'A' | 业务状态,枚举: A :正常 B :提交转下期 C :已转下期 |
| 24 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 25 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统,枚举: 83bfebc8000017ac :总账 import :外部导入 |
| 26 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 27 | flastupdatetime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 28 | frelevancetype | 关联交易类型 | bpchar | 1 |  | √ | '1' | 关联交易类型,枚举: 1 :债权债务 2 :内部往来 3 :损益 4 :现金流量 |
| 29 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 30 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 31 | fisinitrecord | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 32 | fnumber | 凭证编码 | varchar | 50 |  | √ | ' ' | 凭证编码 |
| 33 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fvchcreatorid | 制单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ict_relcfrecord |  | fvoucherid |
| 2 | idx_ict_relcfcord_oops |  | forgid,foporgid,fperiodid,fschemeid |
| 3 | pk_t_ict_relcfrecord |  | fid |

# 数据中间表-pa_dsanalysisdata

## 数据中间表-主表 t_pa_dsanalysisdata

- **表名称：** 数据中间表-主表
- **表名：** t_pa_dsanalysisdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassistantdata1 | ##辅助资料1 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | fextid | 外部ID | varchar | 64 |  | √ | ' ' | 外部ID |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftext10 | ##文本10 | varchar | 100 |  | √ | ' ' | ##文本10 |
| 6 | fassistantdata12 | ##辅助资料12 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 7 | fdecimal4 | ##小数4 | numeric | 23 | 10 | √ | 0 | ##小数4 |
| 8 | fassistantdata11 | ##辅助资料11 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 9 | fdecimal3 | ##小数3 | numeric | 23 | 10 | √ | 0 | ##小数3 |
| 10 | fassistantdata10 | ##辅助资料10 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 11 | fdecimal6 | ##小数6 | numeric | 23 | 10 | √ | 0 | ##小数6 |
| 12 | fdecimal5 | ##小数5 | numeric | 23 | 10 | √ | 0 | ##小数5 |
| 13 | fassistantdata16 | ##辅助资料16 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 14 | fdecimal8 | ##小数8 | numeric | 23 | 10 | √ | 0 | ##小数8 |
| 15 | fassistantdata15 | ##辅助资料15 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 16 | fdecimal7 | ##小数7 | numeric | 23 | 10 | √ | 0 | ##小数7 |
| 17 | fassistantdata14 | ##辅助资料14 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 18 | fassistantdata13 | ##辅助资料13 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 19 | fdecimal9 | ##小数9 | numeric | 23 | 10 | √ | 0 | ##小数9 |
| 20 | fassistantdata7 | ##辅助资料7 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 21 | fassistantdata6 | ##辅助资料6 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 22 | fassistantdata19 | ##辅助资料19 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 23 | fassistantdata9 | ##辅助资料9 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 24 | fassistantdata18 | ##辅助资料18 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 25 | fassistantdata8 | ##辅助资料8 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 26 | fassistantdata17 | ##辅助资料17 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 27 | fassistantdata3 | ##辅助资料3 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 28 | fassistantdata2 | ##辅助资料2 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 29 | fbatchid | 批次 | varchar | 64 |  | √ | ' ' | 批次 |
| 30 | fassistantdata5 | ##辅助资料5 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 31 | ftext1 | ##文本1 | varchar | 100 |  | √ | ' ' | ##文本1 |
| 32 | fdecimal2 | ##小数2 | numeric | 23 | 10 | √ | 0 | ##小数2 |
| 33 | fassistantdata4 | ##辅助资料4 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 34 | ftext2 | ##文本2 | varchar | 100 |  | √ | ' ' | ##文本2 |
| 35 | fdecimal1 | ##小数1 | numeric | 23 | 10 | √ | 0 | ##小数1 |
| 36 | ftext3 | ##文本3 | varchar | 100 |  | √ | ' ' | ##文本3 |
| 37 | ftext4 | ##文本4 | varchar | 100 |  | √ | ' ' | ##文本4 |
| 38 | ftext5 | ##文本5 | varchar | 100 |  | √ | ' ' | ##文本5 |
| 39 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 分析期间 pa_analysisperiod |
| 40 | ftext6 | ##文本6 | varchar | 100 |  | √ | ' ' | ##文本6 |
| 41 | ftext7 | ##文本7 | varchar | 100 |  | √ | ' ' | ##文本7 |
| 42 | ftext8 | ##文本8 | varchar | 100 |  | √ | ' ' | ##文本8 |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | ftext9 | ##文本9 | varchar | 100 |  | √ | ' ' | ##文本9 |
| 45 | fdecimal10 | ##小数10 | numeric | 23 | 10 | √ | 0 | ##小数10 |
| 46 | fassistantdata20 | ##辅助资料20 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 47 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 48 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 科目 pa_account |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_dsanalysisdata |  | fid |
| 2 | uk_pa_dsanalysisdata |  | fextid |

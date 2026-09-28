# 财务报告-fgptas_report

## 财务报告-多语言表 t_fgptas_report_l

- **表名称：** 财务报告-多语言表
- **表名：** t_fgptas_report_l

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
| 1 | pk_fgptas_report_l |  | fpkid |
| 2 | idx_fgptas_report_l |  | fid,flocaleid |

---

## 财务报告-主表 t_fgptas_report

- **表名称：** 财务报告-主表
- **表名：** t_fgptas_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmodel | 报告模板 | int8 | 64 |  | √ | 0 | 财务报告模版 fgptas_fireport_template |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fperiodzone | 期间类型 | varchar | 15 |  | √ | ' ' | 期间类型,枚举: Monthly :月报 Quarterly :季报 HalfYear :半年报 Year :年报 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fentity | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftype | 报告类型 | int8 | 64 |  | √ | 0 | 财务报告类型 fgptas_report_type |
| 14 | fperiod_startdate | 会计期间.开始 | timestamp | 0 |  |  | null | 会计期间.开始 |
| 15 | fyear | 财年 | varchar | 50 |  | √ | ' ' | 财年 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | furl | 报告链接 | varchar | 500 |  | √ | ' ' | 报告链接 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fperiod_enddate | 会计期间.结束 | timestamp | 0 |  |  | null | 会计期间.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_report |  | fid |
| 2 | idx_fgptas_report_number |  | fnumber |

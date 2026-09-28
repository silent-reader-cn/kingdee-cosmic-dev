# 首页关键指标-xkrpt_home_kpi

## 首页关键指标-主表 t_xkrpt_home_kpi

- **表名称：** 首页关键指标-主表
- **表名：** t_xkrpt_home_kpi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frptitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | frptitem | 报表项目 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fkpititle | 指标标题 | varchar | 250 |  | √ | ' ' | 指标标题 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_home_kpi_title |  | fkpititle |
| 2 | pk_xkrpt_home_kpi |  | fid |

---

## 首页关键指标-多语言表 t_xkrpt_home_kpi_l

- **表名称：** 首页关键指标-多语言表
- **表名：** t_xkrpt_home_kpi_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkpititle | 指标标题 | varchar | 250 |  | √ | ' ' | 指标标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_home_kpi_l |  | fpkid |
| 2 | idx_xkrpt_home_kpi_l_fid |  | fid |

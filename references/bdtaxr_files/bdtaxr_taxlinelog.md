# 税行计算日志-bdtaxr_taxlinelog

## 税行计算日志-多语言表 t_bdtaxr_taxlinelog_l

- **表名称：** 税行计算日志-多语言表
- **表名：** t_bdtaxr_taxlinelog_l

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
| 1 | idx_bdtaxr_taxlinelog_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_taxlinelog_l |  | fpkid |

---

## 税行计算日志-主表 t_bdtaxr_taxlinelog

- **表名称：** 税行计算日志-主表
- **表名：** t_bdtaxr_taxlinelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fbilllname | 单据名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fbillid | 调用单据id | int8 | 64 |  | √ | 0 | 调用单据id |
| 10 | flognumber | 日志编号 | varchar | 200 |  | √ | ' ' | 日志编号 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 13 | ftaxresults | 计税结果 | varchar | 50 |  | √ | ' ' | 计税结果,枚举: allSucc :成功 partSucc :部分成功 fail :失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_taxlinelog |  | fnumber |
| 2 | pk_bdtaxr_taxlinelog |  | fid |

# 外汇报价-md_forexquote_f7

## 外汇报价-主表 t_md_forexquote

- **表名称：** 外汇报价-主表
- **表名：** t_md_forexquote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 7 | fpriceruleid | fpriceruleid | int8 | 64 |  | √ | 0 |  |
| 8 | fviewdateaxisid | fviewdateaxisid | int8 | 64 |  | √ | 0 |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fissuezoneid | 发布时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 14 | fissuetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 15 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 16 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 17 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 18 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 19 | fdatatype | fdatatype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_forexquote |  | fid |
| 2 | idx_md_forexquote_b |  | fbillno |

---

## 外汇报价-多语言表 t_md_forexquote_l

- **表名称：** 外汇报价-多语言表
- **表名：** t_md_forexquote_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_forexquote_l |  | fpkid |
| 2 | idx_md_forexquote_l_id |  | fid,flocaleid |

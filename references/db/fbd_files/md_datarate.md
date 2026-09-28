# 参考利率数据-md_datarate

## 参考利率数据-主表 t_md_datarate

- **表名称：** 参考利率数据-主表
- **表名：** t_md_datarate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | freferrateid | 参考利率编码 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fmodifytime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fbizdate | 报价日期 | timestamp | 0 |  |  | null | 报价日期 |
| 12 | fendprice | 利率值（%） | numeric | 23 | 10 | √ | 0.0000000000 | 利率值（%） |
| 13 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 14 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fbeginprice | fbeginprice | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_datarate |  | freferrateid,fbizdate,fendprice |
| 2 | pk_t_md_datarate |  | fid |

---

## 参考利率数据-多语言表 t_md_datarate_l

- **表名称：** 参考利率数据-多语言表
- **表名：** t_md_datarate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_datarate_id |  | fid,flocaleid |
| 2 | pk_t_md_datarate_l |  | fpkid |

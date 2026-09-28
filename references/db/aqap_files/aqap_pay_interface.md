# 银行接口维护-aqap_pay_interface

## 银行接口维护-多语言表 t_aqap_pay_interface_l

- **表名称：** 银行接口维护-多语言表
- **表名：** t_aqap_pay_interface_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 接口说明 | varchar | 255 |  | √ | ' ' | 接口说明 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cluster_pay_interface_l |  | fname |
| 2 | pk_aqap_pay_interface_l |  | fpkid |
| 3 | idx_aqap_pay_interface_l_0 |  | fid,flocaleid |

---

## 银行接口维护-主表 t_aqap_pay_interface

- **表名称：** 银行接口维护-主表
- **表名：** t_aqap_pay_interface

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 银行版本 | int8 | 64 |  | √ | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 3 | fname | 接口说明 | varchar | 100 |  | √ | ' ' | 接口说明 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbiz_type | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 aqap_business_type](../aqap_files/aqap_business_type.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fclass_name | 接口实现类名 | varchar | 500 |  | √ | ' ' | 接口实现类名 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编号 | varchar | 100 |  | √ | ' ' | 编号 |
| 14 | fdesc | fdesc | varchar | 50 |  | √ | ' ' |  |
| 15 | flimit_num | 每批最大笔数 | int8 | 64 |  | √ | 0 | 每批最大笔数 |
| 16 | fbank_code | 接口代码 | varchar | 150 |  | √ | ' ' | 接口代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_pay_interface |  | fid |
| 2 | idx_cluster_pay_interface |  | fnumber |

# 单元测试DEMO单据-isc_unittest_demo_bill

## 单元测试DEMO单据-主表 t_isc_unittest_demo_bill

- **表名称：** 单元测试DEMO单据-主表
- **表名：** t_isc_unittest_demo_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftestbase | 单元测试基础资料 | int8 | 64 |  | √ | 0 | 单元测试DEMO基础资料 isc_unittest_demo_base |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_unittest_demo_bill |  | fbillno |
| 2 | t_isc_unittest_demo_bill_pkey |  | fid |

---

## 附件-附件表 t_isc_unit_entry_field

- **表名称：** 附件-附件表
- **表名：** t_isc_unit_entry_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_isc_unit_entry_field |  | fpkid |
| 2 | idx_isc_unit_entry_field_1 |  | fentryid |

---

## 详情-子表 t_isc_unittest_entry

- **表名称：** 详情-子表
- **表名：** t_isc_unittest_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagefield | 年龄 | int8 | 64 |  | √ | 0 | 年龄 |
| 3 | fbirthday | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 4 | fnamefield | 姓名 | varchar | 100 |  | √ | ' ' | 姓名 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_unittest_entry |  | fnamefield |
| 2 | t_isc_unittest_entry_pkey |  | fentryid |

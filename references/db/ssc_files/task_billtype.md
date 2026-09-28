# 业务单据-task_billtype

## 业务单据-多语言表 t_tk_bill_l

- **表名称：** 业务单据-多语言表
- **表名：** t_tk_bill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_bill_l_pkey |  | fpkid |
| 2 | idx_tk_billl_locale |  | fid,flocaleid |

---

## 单据体-子表 t_tk_billtaskentry

- **表名称：** 单据体-子表
- **表名：** t_tk_billtaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskcreateruleid | 任务创建规则ID | int8 | 64 |  | √ | 0 | 任务创建规则ID |
| 3 | ftasktypeid | 任务类型id | int8 | 64 |  | √ | 0 | 任务类型id |
| 4 | ftasktypenumber | 任务类型编码 | varchar | 80 |  | √ | ' ' | 任务类型编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftasktypename | 任务类型名称 | varchar | 80 |  | √ | ' ' | 任务类型名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_billtaskentry |  | ftasktypeid |
| 2 | t_tk_billtaskentry_pkey |  | fid |

---

## 二级分类配置-子表 t_tk_divisionentry

- **表名称：** 二级分类配置-子表
- **表名：** t_tk_divisionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasename | 基础资料名字 | varchar | 50 |  | √ | ' ' | 基础资料名字 |
| 3 | ffieldselect | 字段选择 | varchar | 50 |  | √ | ' ' | 字段选择 |
| 4 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 5 | fentrycoefficient | 标准系数 | numeric | 23 | 2 | √ | 0.00 | 标准系数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffieldselectkey | 字段选择key | varchar | 50 |  | √ | ' ' | 字段选择key |
| 9 | fcomparingvalue | 比较值后台值 | varchar | 50 |  | √ | ' ' | 比较值后台值 |
| 10 | fcomparingname | 比较值 | varchar | 50 |  | √ | ' ' | 比较值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_divisionentry_pkey |  | fentryid |
| 2 | index_ssc_divisionentry |  | fid |

---

## 业务单据-主表 t_tk_bill

- **表名称：** 业务单据-主表
- **表名：** t_tk_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbindbill | 绑定单据实体 | varchar | 50 |  | √ | ' ' | 绑定单据实体 |
| 3 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbindformnumber | 绑定界面编码 | varchar | 80 |  | √ | ' ' | 绑定界面编码 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbindform | 绑定展示界面 | varchar | 50 |  | √ | ' ' | 绑定展示界面 |
| 8 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbindbillnumber | 绑定单据编码 | varchar | 80 |  | √ | ' ' | 绑定单据编码 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | bindbill2 | bindbill2 | varchar | 36 |  | √ | ' ' |  |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fexternalerpid | 所属系统 | int8 | 64 |  | √ | 0 | 业务系统 bas_extenderp |
| 16 | fcoefficient | 标准系数 | numeric | 23 | 10 | √ | 0.0000000000 | 标准系数 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_bill |  | fbindbill |
| 2 | t_tk_bill_pkey |  | fid |

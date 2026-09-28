# 付款接口规则设置-aqap_pay_rule_config

## 单据体-子表 t_aqap_pay_rule

- **表名称：** 单据体-子表
- **表名：** t_aqap_pay_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 4 | fcreatetime | fcreatetime | int8 | 64 |  |  | null |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 7 | flogic | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: & :并且 |
| 8 | fmodifytime | fmodifytime | int8 | 64 |  |  | null |  |
| 9 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fkey | 匹配字段 | varchar | 50 |  | √ | ' ' | 匹配字段,枚举: subBizType :子业务类型 amount :金额 currency :币种 explanation :付款摘要 sameBank :同行 individual :对私 useCn :用途 merge :加急 |
| 12 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: = :等于 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 15 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cluster_pay_rule |  | fkey |
| 2 | idx_aqap_pay_rule_fk |  | fid |
| 3 | pk_aqap_pay_rule |  | fentryid |

---

## 付款接口规则设置-多语言表 t_aqap_pay_rule_config_l

- **表名称：** 付款接口规则设置-多语言表
- **表名：** t_aqap_pay_rule_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_pay_rule_config_l_0 |  | fid,flocaleid |
| 2 | idx_cluster_pay_rule_config_l |  | fname |
| 3 | pk_aqap_pay_rule_config_l |  | fpkid |

---

## 付款接口规则设置-主表 t_aqap_pay_rule_config

- **表名称：** 付款接口规则设置-主表
- **表名：** t_aqap_pay_rule_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbd_interface | 付款接口代码 | int8 | 64 |  | √ | 0 | 银行接口维护 aqap_pay_interface |
| 3 | fgroupid | 银行版本 | int8 | 64 |  | √ | 0 | 银行启用管理 aqap_bank |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 14 | fsort_num | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_pay_rule_config |  | fid |
| 2 | idx_cluster_pay_rule_config |  | fnumber |

# 输入参数-plm_rengine_sceneinput

## 输入参数-主表 t_plm_egn_sceneinput

- **表名称：** 输入参数-主表
- **表名：** t_plm_egn_sceneinput

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 3 | fmultiple | 支持多选 | bpchar | 1 |  | √ | '1' | 支持多选 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 2 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fdynprop | 属性字段 | varchar | 50 |  | √ | ' ' | 属性字段 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fparamstype | 参数类型 | varchar | 20 |  | √ | ' ' | 参数类型,枚举: dynamicObject :业务对象字段 basedata :基础资料 string :字符串 number :数字 boolean :布尔 date :日期 enum :枚举 |
| 10 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | findex | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 15 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 17 | ftreelv | 属性字段层级 | int8 | 64 |  | √ | 0 | 属性字段层级 |
| 18 | fparamsobject | 业务对象 | varchar | 100 |  | √ | ' ' | 主实体对象（规则引擎） plm_rengine_entityobject |
| 19 | fpresetisedit | 预置是否已更新 | bpchar | 1 |  | √ | '0' | 预置是否已更新 |
| 20 | fdateformat | 掩码 | varchar | 30 |  | √ | ' ' | 掩码,枚举: yyyy-MM-dd :YYYY-MM-DD yyyy/MM/dd :YYYY/MM/DD yy-MM/dd :YY-MM/DD yyyy-MM :YYYY-MM yyyy/MM :YYYY/MM yyyy :YYYY |
| 21 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 22 | fbasedatafield | 基础资料 | varchar | 36 |  | √ | ' ' | 主实体对象（规则引擎） plm_rengine_entityobject |
| 23 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 10 :待启用 |
| 24 | fnumber | 参数标识 | varchar | 100 |  | √ | ' ' | 参数标识 |
| 25 | fcombofield | 下拉项 | varchar | 2000 |  | √ | ' ' | 下拉项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_sceneinput |  | fid |
| 2 | idx_plm_sceneinput |  | fid |

---

## 输入参数-多语言表 t_plm_egn_sceneinput_l

- **表名称：** 输入参数-多语言表
- **表名：** t_plm_egn_sceneinput_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 3 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_sceneinput_l |  | fpkid |
| 2 | idx_plm_sceneinput_l |  | fid,flocaleid |

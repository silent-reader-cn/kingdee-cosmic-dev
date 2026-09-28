# 输出参数-plm_rengine_sceneoutput

## 输出参数-多语言表 t_plm_egn_sceneoutput_l

- **表名称：** 输出参数-多语言表
- **表名：** t_plm_egn_sceneoutput_l

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
| 1 | idx_plm_sceneoutput_l |  | fid,flocaleid |
| 2 | pk_plm_egn_sceneoutput_l |  | fpkid |

---

## 输出参数-主表 t_plm_egn_sceneoutput

- **表名称：** 输出参数-主表
- **表名：** t_plm_egn_sceneoutput

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | findex | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmultiple | 允许多选 | bpchar | 1 |  | √ | '1' | 允许多选 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fparamsobject | 业务对象 | varchar | 100 |  | √ | ' ' | 主实体对象（规则引擎） plm_rengine_entityobject |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fpresetisedit | 预置是否已更新 | bpchar | 1 |  | √ | '0' | 预置是否已更新 |
| 13 | fdateformat | 掩码 | varchar | 30 |  | √ | ' ' | 掩码,枚举: yyyy-MM-dd :YYYY-MM-DD yyyy/MM/dd :YYYY/MM/DD yy-MM/dd :YY-MM/DD yyyy-MM :YYYY-MM yyyy/MM :YYYY/MM yyyy :YYYY |
| 14 | fstatus | 数据状态 | varchar | 2 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fdynprop | 属性字段 | varchar | 50 |  | √ | ' ' | 属性字段 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 19 | fbasedatafield | 基础资料 | varchar | 36 |  | √ | ' ' | 主实体对象（规则引擎） plm_rengine_entityobject |
| 20 | fenable | 使用状态 | varchar | 2 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 10 :待启用 |
| 21 | fparamstype | 参数类型 | varchar | 20 |  | √ | ' ' | 参数类型,枚举: dynamicObject :业务对象字段 basedata :基础资料 string :字符串 number :数字 boolean :布尔 date :日期 enum :枚举 |
| 22 | fnumber | 参数标识 | varchar | 100 |  | √ | ' ' | 参数标识 |
| 23 | fissyspreset | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 24 | fcombofield | 下拉项 | varchar | 2000 |  |  | ' ' | 下拉项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_sceneoutput |  | fid |
| 2 | idx_plm_sceneoutput |  | fid |

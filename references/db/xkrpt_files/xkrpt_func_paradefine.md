# 取数参数管理-xkrpt_func_paradefine

## 取数参数管理-主表 t_xkrpt_func_paradefine

- **表名称：** 取数参数管理-主表
- **表名：** t_xkrpt_func_paradefine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fassistantfield | 参数关联类型 | varchar | 50 |  | √ | ' ' | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 11 | fbasedatafield | 参数关联类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fparatype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: basedatafield :基础资料 assistantfield :辅助资料 integerfield :整数 datefield :日期 textfield :文本 decimalfield :数值 combofield :下拉列表 timefield :时间 checkboxfield :复选框 |
| 14 | fnumber | 参数编码 | varchar | 50 |  | √ | ' ' | 参数编码 |
| 15 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 16 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_func_paradefine |  | fid |
| 2 | idx_xkrpt_func_pd_fnumber |  | fnumber |

---

## 取数参数管理-多语言表 t_xkrpt_func_paradefine_l

- **表名称：** 取数参数管理-多语言表
- **表名：** t_xkrpt_func_paradefine_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 3 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_func_pd_l_fid |  | fid,flocaleid |
| 2 | pk_t_xkrpt_func_paradefine_l |  | fpkid |

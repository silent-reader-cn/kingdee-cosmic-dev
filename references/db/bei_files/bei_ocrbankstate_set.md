# 文件识别配置-bei_ocrbankstate_set

## 文件识别配置-多语言表 t_bei_ocrbankstate_set_l

- **表名称：** 文件识别配置-多语言表
- **表名：** t_bei_ocrbankstate_set_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 银行名称 | varchar | 80 |  | √ | ' ' | 银行名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_ocrbankstate_set_l |  | fpkid |
| 2 | idx_t_bei_ocrbankstate_set_l |  | fid |

---

## 文件识别配置-主表 t_bei_ocrbankstate_set

- **表名称：** 文件识别配置-主表
- **表名：** t_bei_ocrbankstate_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 银行名称 | varchar | 80 |  | √ | ' ' | 银行名称 |
| 3 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fexeclasspath | 执行类 | varchar | 255 |  | √ | ' ' | 执行类 |
| 5 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 11 | fkeyword | 关键字 | varchar | 255 |  | √ | ' ' | 关键字 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_ocrbankstate_set |  | fenable |
| 2 | pk_t_bei_ocrbankstate_set |  | fid |

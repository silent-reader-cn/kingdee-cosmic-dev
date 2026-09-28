# 税务参数-tctb_taxparam

## 税务参数-主表 t_tctb_taxparam

- **表名称：** 税务参数-主表
- **表名：** t_tctb_taxparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmulvalue | 参数值 | varchar | 50 |  | √ | ' ' | 参数值,枚举: |
| 7 | favalibleval | 参数可选值 | varchar | 200 |  | √ | ' ' | 参数可选值 |
| 8 | fparamval | fparamval | varchar | 50 |  | √ | ' ' |  |
| 9 | forg | 业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fparamkey | 参数控件标识 | varchar | 50 |  | √ | ' ' | 参数控件标识 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fparamvalue | 参数值 | varchar | 50 |  | √ | ' ' | 参数值,枚举: |
| 16 | fismultiple | 是否多选 | varchar | 50 |  | √ | ' ' | 是否多选 |
| 17 | fparamname | 参数名称 | varchar | 200 |  | √ | ' ' | 参数名称 |
| 18 | fpagekey | 页面标识 | varchar | 50 |  | √ | ' ' | 页面标识 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_taxparam |  | fid |
| 2 | idx_t_tctb_taxparam_org |  | forg |

---

## 税务参数-多语言表 t_tctb_taxparam_l

- **表名称：** 税务参数-多语言表
- **表名：** t_tctb_taxparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxparam_l_0 |  | fid,flocaleid |
| 2 | pk_tctb_taxparam_l |  | fpkid |

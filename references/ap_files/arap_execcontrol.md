# 事中控制-arap_execcontrol

## 事中控制-多语言表 t_arap_execcontrol_l

- **表名称：** 事中控制-多语言表
- **表名：** t_arap_execcontrol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arap_execcontrol_l |  | fpkid |
| 2 | idx_arap_execcontrol_l_fid |  | fid,flocaleid |

---

## 事中控制-主表 t_arap_execcontrol

- **表名称：** 事中控制-主表
- **表名：** t_arap_execcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fispreinsert | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fapptype | 应用 | varchar | 30 |  | √ | ' ' | 应用,枚举: ar :应收 ap :应付 |
| 7 | fctrlmode | 控制方式 | varchar | 30 |  | √ | ' ' | 控制方式,枚举: plugin :插件 customize :自定义 |
| 8 | fctrlpoint | 控制时机 | varchar | 50 |  | √ | ' ' | 控制时机,枚举: save :保存 submit :提交 audit :审核 delete :删除 |
| 9 | ftips | 提示信息 | varchar | 255 |  | √ | ' ' | 提示信息 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fctrlexplain | 控制说明 | varchar | 255 |  | √ | ' ' | 控制说明 |
| 15 | fctrltype | 控制类型 | varchar | 30 |  | √ | ' ' | 控制类型,枚举: warn :提醒 error :禁止 |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fbizobjid | 控制对象 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 18 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 19 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arap_execcontrol_number |  | fnumber |
| 2 | pk_t_arap_execcontrol |  | fid |

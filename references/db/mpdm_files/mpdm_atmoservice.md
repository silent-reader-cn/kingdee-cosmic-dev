# 制造云服务-mpdm_atmoservice

## 制造云服务-多语言表 t_mpdm_atmcop_l

- **表名称：** 制造云服务-多语言表
- **表名：** t_mpdm_atmcop_l

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
| 1 | idx_mpdm_atmcop_l |  | fid,flocaleid |
| 2 | t_mpdm_atmcop_l_pkey |  | fpkid |

---

## 制造云服务-主表 t_mpdm_atmcop

- **表名称：** 制造云服务-主表
- **表名：** t_mpdm_atmcop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmethodname | 方法名 | varchar | 50 |  | √ | ' ' | 方法名 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fclasspath | 插件路径 | varchar | 255 |  | √ | ' ' | 插件路径 |
| 9 | freturnval | freturnval | varchar | 50 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 12 | fappid | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | finparam | finparam | varchar | 255 |  | √ | ' ' |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcloudid | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 18 | fservicename | 接口名 | varchar | 50 |  | √ | ' ' | 接口名 |
| 19 | fisms | 通用服务 | bpchar | 1 |  | √ | ' ' | 通用服务 |
| 20 | fperiod | 执行阶段 | varchar | 30 |  | √ | ' ' | 执行阶段,枚举: all :全程 onPreparePropertys :字段准备 onAddValidators :添加校验器 beforeExecuteOperation :操作前 beginOperationTransaction :操作开始 endOperationTransaction :操作结束 rollbackOperation :回滚 afterExecuteOperation :操作后 |
| 21 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fdataentitynum | 参数表单 | varchar | 50 |  | √ | ' ' | 参数表单 |
| 24 | fopdescrip | 操作描述 | varchar | 255 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_atmcop |  | fnumber,fcreateorgid |
| 2 | t_mpdm_atmcop_pkey |  | fid |

---

## 单据体-子表 t_mpdm_atmoentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_atmoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: int :整型 long :长整型 double :浮点数 string :字符串 date :日期 time :时间 boolean :布尔值 object :未定 |
| 3 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fismust | 必录 | bpchar | 1 |  | √ | ' ' | 必录 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_atmoentry |  | fid,fseq |
| 2 | pk_t_mpdm_atmoentry |  | fentryid |

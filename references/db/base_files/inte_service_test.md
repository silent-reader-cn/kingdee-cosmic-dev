# 国际化接口测试-inte_service_test

## 国际化接口测试-多语言表 t_int_servicetest_l

- **表名称：** 国际化接口测试-多语言表
- **表名：** t_int_servicetest_l

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
| 1 | idx_t_int_stest_l_fid |  | fid |
| 2 | pk_t_int_servicetest_l |  | fpkid |

---

## 单据体-子表 t_int_servicetest_entry

- **表名称：** 单据体-子表
- **表名：** t_int_servicetest_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | finparam | 入参 | varchar | 2000 |  | √ | ' ' | 入参 |
| 4 | ftestcase | 用例名 | varchar | 500 |  | √ | ' ' | 用例名 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fexpectedresult | 预期结果 | varchar | 2000 |  | √ | ' ' | 预期结果 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_stest_fid |  | fid |
| 2 | pk_t_int_servicetest_entry |  | fentryid |

---

## 国际化接口测试-主表 t_int_servicetest

- **表名称：** 国际化接口测试-主表
- **表名：** t_int_servicetest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmethodname | 方法名 | varchar | 50 |  | √ | ' ' | 方法名 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fuserid | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcloudname | 云名称 | varchar | 50 |  | √ | ' ' | 云名称 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :微服务接口 1 :反射 2 :脚本 |
| 12 | frefclassname | 反射类名 | varchar | 500 |  | √ | ' ' | 反射类名 |
| 13 | frefargsname | 反射方法参数 | varchar | 500 |  | √ | ' ' | 反射方法参数 |
| 14 | fappname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 15 | fservicename | 服务名 | varchar | 50 |  | √ | ' ' | 服务名 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | frefmethodname | 反射方法名 | varchar | 500 |  | √ | ' ' | 反射方法名 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_servicetest |  | fid |
| 2 | idx_t_int_stest_fnum |  | fnumber |
